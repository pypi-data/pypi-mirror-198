import psycopg2
import pandas as pd
import numpy as np
import json
import os
import subprocess
import uuid
from urllib.parse import urlencode
import boto3
import requests
import yandexcloud
import datetime as dt
from yandex.cloud.lockbox.v1.payload_service_pb2 import GetPayloadRequest
from yandex.cloud.lockbox.v1.payload_service_pb2_grpc import PayloadServiceStub
import pandas.io.sql as psql

boto_session = None

def get_boto_session():
    global boto_session
    if boto_session is not None:
        return boto_session

    # initialize lockbox and read secret value
    yc_sdk = yandexcloud.SDK()
    channel = yc_sdk._channels.channel("lockbox-payload")
    lockbox = PayloadServiceStub(channel)
    response = lockbox.Get(GetPayloadRequest(secret_id=os.environ['SECRET_ID']))

    # extract values from secret
    access_key = None
    secret_key = None
    for entry in response.entries:
        if entry.key == 'ACCESS_KEY_ID':
            access_key = entry.text_value
        elif entry.key == 'SECRET_ACCESS_KEY':
            secret_key = entry.text_value
    if access_key is None or secret_key is None:
        raise Exception("secrets required")

    # initialize boto session
    boto_session = boto3.session.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    return boto_session


conn = psycopg2.connect(
    dbname='tel_aol', # Идентификатор подключения
    user="bot", # Пользователь БД
    password="botpassword",
    host="rc1a-oxmhyenirdrebhdx.mdb.yandexcloud.net", # Точка входа
    port=6432,
    sslmode="require")
cursor = conn.cursor()

def insertIntoTable(df, table, cur=cursor, conn=conn):
    tuples = list(set([tuple(x) for x in df.to_numpy(na_value = None)]))
    cols = ','.join(list(df.columns))
    col_l = []
    for i in list(df.columns):
        col_l.append('%s')
    s = ','.join(col_l)
    query = f"INSERT INTO {table}({cols}) VALUES({s})"
    try:
        cur.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        return 1

def archiveRows(ids, table, index, cur=cursor, conn=conn):
    query = f"UPDATE {table} SET updated_at = '{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' WHERE {index} in ({ids}) and updated_at is null"
    try:
        cur.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        return 1

def updateTable(table, df, columns_dict, common_id = False, amount = 1000, nohub=False, ready=False, cursor=cursor, conn=conn):
    df = df.rename(columns=columns_dict, errors="raise")
    print(df)
    index_name = table+'_id'
    if not common_id:
        df[index_name] += major_id * amount
    filt = '1=1' if common_id else f'{index_name} >= {str(major_id*amount)} and {index_name} < {str((major_id+1)*amount)}'
    if not nohub:
        cursor.execute(f'SELECT * FROM public.hub_{table} where {filt}')
        edata = cursor.fetchall()
        ed_cols = []
        for col in cursor.description:
            ed_cols.append(col[0])
        ed = pd.DataFrame(data=edata,columns=ed_cols)
        ed_id_list = ed[index_name].values.tolist()
        if ed_id_list==[]:
            df_temp = pd.DataFrame(df, columns=[index_name])
            df_temp['created_at'] = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            insertIntoTable(df_temp, f'hub_{table}')
        else:
            nd_id_list=df[index_name].values.tolist()
            new_id_list = []
            for element in nd_id_list:
                if element not in ed_id_list:
                    new_id_list.append(element)
            new_df = df[df[index_name].isin(new_id_list)]
            new_df = pd.DataFrame(new_df, columns=[index_name])
            new_df['created_at'] = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if new_df.shape[0]>0:
                insertIntoTable(new_df, f'hub_{table}')
    table = 'sat_' + table
    cursor.execute(f'SELECT * FROM public.{table} WHERE updated_at is null and {filt}')
    edata = cursor.fetchall()
    ed_cols = []
    for col in cursor.description:
        ed_cols.append(col[0])
    ed = pd.DataFrame(data=edata,columns=ed_cols)
    ed_id_list = ed[index_name].values.tolist()
    #print(ed_id_list)
    #print(df)

    if ed_id_list==[]:
        df['update_reason'] = 'created'
        df['created_at'] = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insertIntoTable(df, table)
        return 1
    nd_id_list=df[index_name].values.tolist()
    archive_id_list = []
    for element in ed_id_list:
        if element not in nd_id_list:
            archive_id_list.append(element)

    new_df = df[~df[index_name].isin(ed_id_list)]
    new_df = pd.DataFrame(new_df)
    new_df['update_reason'] = 'created'
    #print('new_df')
    #print(new_df)

    old_df = df[df[index_name].isin(ed_id_list)]
    old_df = old_df.set_index(index_name).drop_duplicates()
    old_df.sort_index(inplace=True)
    #print('old_df')
    #print(old_df)

    ed = ed[ed[index_name].isin(old_df.index.values.tolist())]
    ed = ed.set_index(index_name)
    ed_comp = pd.DataFrame(ed, columns=list(old_df.columns), dtype=None, copy=None)
    ed_comp.sort_index(inplace=True)
    #print('ed_comp')
    #print(ed_comp)

    compare = ed_comp.compare(old_df)
    old_df = old_df.reset_index(level=0)
    changed = old_df[old_df[index_name].isin(compare.index.values.tolist())]
    changed = pd.DataFrame(changed)
    changed['update_reason'] = 'updated'
    #print('changed')
    #print(changed)

    changed_id_list = changed[index_name].values.tolist()
    archive_id_list += changed_id_list
    archive_ids = ','.join(str(e) for e in archive_id_list)

    draft_new = pd.concat([new_df, changed])
    #print('draft_new')
    #print(draft_new)

    new = pd.DataFrame(draft_new, columns=df.columns.tolist()+['update_reason'])

    new['created_at'] = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #print('new')
    #print(new)

    if len(archive_ids)>0:
        archiveRows(archive_ids, table, index_name)

    if new.shape[0]>0:
        insertIntoTable(new, table)
    
def handler(event, context):
    session = get_boto_session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )

    get_object_response = s3.get_object(Bucket=event['messages'][0]['details']['bucket_id'],Key=event['messages'][0]['details']['object_id'])
    with open('/tmp/file.xlsx', 'wb') as xlsx:
        xlsx.write(get_object_response['Body'].read())

    student = pd.read_excel('/tmp/file.xlsx', sheet_name='student')
    print(student)
    updateTable('student', student, columns_dict={"ST number": "student_id", "Student name": "student_name", "Admission year": "admission_year", "Graduation year": "graduation_year"}, common_id = True, amount = 1000, nohub=False, ready=False, cursor=cursor, conn=conn)
