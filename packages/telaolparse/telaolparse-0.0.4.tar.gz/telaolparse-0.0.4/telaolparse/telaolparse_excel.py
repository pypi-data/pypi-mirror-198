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

def handler(event, context):
    session = get_boto_session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )

    get_object_response = s3.get_object(Bucket=event['messages'][0]['details']['bucket_id'],Key=event['messages'][0]['details']['object_id'])
    with open('/tmp/file.xlsx', 'wb') as xlsx:
        xlsx.write(get_object_response['Body'].read())

    program_info = pd.read_excel('/tmp/file.xlsx', sheet_name='Program info')
    major_id = program_info.iloc[0,1]
    degree = program_info.iloc[1,1]
    program_name = program_info.iloc[2,1]
    major_name = program_info.iloc[3,1]
    try:
        dttm = program_info.iloc[4,1].strftime('%Y-%m-%d %H:%M:%S')
    except:
        dttm = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    major_d = {'major_id': [major_id], 'degree': [degree], 'program_name': [program_name], 'major_name': [major_name]}
    major_df = pd.DataFrame(data=major_d)
    
    courses = pd.read_excel("/tmp/file.xlsx", sheet_name="Curriculum map", usecols=lambda x: x not in ['skip1','skip2','skip3'])
    #print(courses)
    courses = courses.transpose()
    courses = courses.reset_index()
    courses.columns = courses.iloc[0]
    courses = courses[1:]
    courses = courses.replace(regex=r'^Unnamed', value=np.nan)
    courses['Semester'] = courses['Semester'].fillna(method='ffill')
    #print(courses)
    courses_obj_l_df = pd.read_excel("/tmp/file.xlsx", sheet_name="Curriculum map", usecols='D:D',skiprows=4).squeeze("columns")
    courses_obj_list = courses_obj_l_df.values.tolist()
    #print(courses_obj_list)

    courses = courses.replace(regex='^c$', value=False)
    courses = courses.replace(regex='^e$', value=True)
    courses['Course status (core/elective)']=courses['Course status (core/elective)'].astype(bool)
    courses_df=courses.drop(columns=courses_obj_list)
    #print('courses_df')
    #print(courses_df.columns)
    courses_obj = pd.DataFrame(courses, columns=courses_obj_list+['CourseID'], dtype=None, copy=None)
    courses_obj.set_index('CourseID', inplace=True)
    #print('courses_obj')
    courses_obj = courses_obj.stack().reset_index()
    #print('stacked_courses_obj')
    #print(courses_obj)
    #print(courses_obj.columns.values.tolist())


    lgo = pd.read_excel('/tmp/file.xlsx', sheet_name='LGO')
    lgo_goals = pd.DataFrame(lgo, columns=['Goal TraitID','Learning goals'], dtype=None, copy=None)
    lgo_goals = lgo_goals.rename(columns={"Goal TraitID": "criterion_id", "Learning goals": "criterion_name"})
    lgo_goals = lgo_goals.fillna(method='ffill', axis=0).drop_duplicates()
    lgo_obj = pd.DataFrame(lgo, columns=['Goal TraitID','Objective TraitID','Learning objectives'], dtype=None, copy=None)
    lgo_obj = lgo_obj.rename(columns={"Goal TraitID": "parent_criterion_id", "Objective TraitID": "criterion_id","Learning objectives": "criterion_name"})
    lgo_obj = lgo_obj.fillna(method='ffill', axis=0).drop_duplicates()
    lgo_traits = pd.DataFrame(lgo, columns=['Objective TraitID','TraitID','Traits','Does not meet expectations (1)','Meets expectations (2)','Exceeds expectations (3)'], dtype=None, copy=None)
    lgo_traits = lgo_traits.rename(columns={"Objective TraitID": "parent_criterion_id", "TraitID": "criterion_id","Traits": "criterion_name",'Does not meet expectations (1)':'trait_does_not_meets_descr','Meets expectations (2)':'trait_meets_descr','Exceeds expectations (3)':'trait_exceeds_descr'})
    lgo_traits = lgo_traits.fillna(method='ffill', axis=0).drop_duplicates()
    for df in [lgo_goals,lgo_obj,lgo_traits]:
        df.criterion_id += major_id * 1000
    for df in [lgo_obj,lgo_traits]:
        df.parent_criterion_id += major_id * 1000
    #sat_criterion = pd.concat([lgo_goals,lgo_obj,lgo_traits])
    #lgo_goals[["criterion_code","parent_criterion_id","trait_exceeds_descr","trait_meets_descr","trait_does_not_meets_descr"]] = 'null'

    artifact = pd.read_excel('/tmp/file.xlsx', sheet_name='Artifact')
    student = pd.read_excel('/tmp/file.xlsx', sheet_name='Students')
    student['major_id'] = major_id

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
            #print("Error: %s" % error)
            conn.rollback()
            return 1
    
    def archiveRows(ids, table, index, cur=cursor, conn=conn, dttm=dttm):
        query = f"UPDATE {table} SET updated_at = '{dttm}' WHERE {index} in ({ids}) and updated_at is null"
        try:
            cur.execute(query)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            #print("Error: %s" % error)
            conn.rollback()
            return 1
    
    cursor.execute(f'SELECT * FROM public.hub_criterion where criterion_id >= {str(major_id*1000)} and criterion_id < {str((major_id+1)*1000)}')
    edata = cursor.fetchall()
    ed_cols = []
    for col in cursor.description:
        ed_cols.append(col[0])
    ed = pd.DataFrame(data=edata,columns=ed_cols)
    ed_id_list = ed.criterion_id.values.tolist()
    if ed_id_list==[]:
        for df in [lgo_goals, lgo_obj, lgo_traits]:
            df_temp = pd.DataFrame(df, columns=['criterion_id'])
            df_temp['created_at'] = dttm
            insertIntoTable(df_temp, 'hub_criterion')
    else:
        nd_id_list=[]
        for df in [lgo_goals, lgo_obj, lgo_traits]:
            df_id=df.criterion_id.values.tolist()
            nd_id_list +=df_id
        new_id_list = []
        for element in nd_id_list:
            if element not in ed_id_list:
                new_id_list.append(element)
        for df in [lgo_goals, lgo_obj, lgo_traits]:
            new_df = df[df.criterion_id.isin(new_id_list)]
            new_df = pd.DataFrame(new_df, columns=['criterion_id'])
            new_df['created_at'] = dttm
            if new_df.shape[0]>0:
                insertIntoTable(new_df, 'hub_criterion')

    cursor.execute(f'SELECT * FROM public.sat_criterion where criterion_id >= {str(major_id*1000)} and criterion_id < {str((major_id+1)*1000)} and updated_at is null')
    edata = cursor.fetchall()
    ed_cols = []
    for col in cursor.description:
        ed_cols.append(col[0])
    ed = pd.DataFrame(data=edata,columns=ed_cols)
    ed_id_list = ed.criterion_id.values.tolist()
    if ed_id_list==[]:
        for df in [lgo_goals, lgo_obj, lgo_traits]:
            df['update_reason'] = 'created'
            df['created_at'] = dttm
            insertIntoTable(df, 'sat_criterion')
    else:
        lgo_goals_id=lgo_goals.criterion_id.values.tolist()
        lgo_obj_id=lgo_obj.criterion_id.values.tolist()
        lgo_traits_id=lgo_traits.criterion_id.values.tolist()
        nd_id_list = lgo_goals_id+lgo_obj_id+lgo_traits_id
        archive_id_list = []
        for element in ed_id_list:
            if element not in nd_id_list:
                archive_id_list.append(element)

        new_lgo_goals = lgo_goals[~lgo_goals.criterion_id.isin(ed_id_list)]
        new_lgo_goals = pd.DataFrame(new_lgo_goals)
        new_lgo_goals['update_reason'] = 'created'
        new_lgo_obj = lgo_obj[~lgo_obj.criterion_id.isin(ed_id_list)]
        new_lgo_obj = pd.DataFrame(new_lgo_obj)
        new_lgo_obj['update_reason'] = 'created'
        new_lgo_traits = lgo_traits[~lgo_traits.criterion_id.isin(ed_id_list)]
        new_lgo_traits = pd.DataFrame(new_lgo_traits)
        new_lgo_traits['update_reason'] = 'created'

        old_lgo_goals = lgo_goals[lgo_goals.criterion_id.isin(ed_id_list)]
        old_lgo_goals = old_lgo_goals.set_index('criterion_id').drop_duplicates()
        old_lgo_goals.sort_index(inplace=True)
        old_lgo_obj = lgo_obj[lgo_obj.criterion_id.isin(ed_id_list)]
        old_lgo_obj = old_lgo_obj.set_index('criterion_id').drop_duplicates()
        old_lgo_obj.sort_index(inplace=True)
        old_lgo_traits = lgo_traits[lgo_traits.criterion_id.isin(ed_id_list)]
        old_lgo_traits = old_lgo_traits.set_index('criterion_id').drop_duplicates()
        old_lgo_traits.sort_index(inplace=True)

        ed_goals = ed[ed.criterion_id.isin(old_lgo_goals.index.values.tolist())]
        ed_goals = ed_goals.set_index('criterion_id')
        ed_goals_comp = pd.DataFrame(ed_goals, columns=list(old_lgo_goals.columns), dtype=None, copy=None)
        ed_goals_comp.sort_index(inplace=True)
        ed_obj = ed[ed.criterion_id.isin(old_lgo_obj.index.values.tolist())]
        ed_obj = ed_obj.set_index('criterion_id')
        ed_obj_comp = pd.DataFrame(ed_obj, columns=list(old_lgo_obj.columns), dtype=None, copy=None)
        ed_obj_comp.sort_index(inplace=True)
        ed_traits = ed[ed.criterion_id.isin(old_lgo_traits.index.values.tolist())]
        ed_traits = ed_traits.set_index('criterion_id')
        ed_traits_comp = pd.DataFrame(ed_traits, columns=list(old_lgo_traits.columns), dtype=None, copy=None)
        ed_traits_comp.sort_index(inplace=True)

        compare_goals = ed_goals_comp.compare(old_lgo_goals)
        old_lgo_goals = old_lgo_goals.reset_index(level=0)
        changed_goals = old_lgo_goals[old_lgo_goals.criterion_id.isin(compare_goals.index.values.tolist())]
        changed_goals = pd.DataFrame(changed_goals)
        changed_goals['update_reason'] = 'updated'

        compare_obj = ed_obj_comp.compare(old_lgo_obj)
        old_lgo_obj = old_lgo_obj.reset_index(level=0)
        changed_obj = old_lgo_obj[old_lgo_obj.criterion_id.isin(compare_obj.index.values.tolist())]
        changed_obj = pd.DataFrame(changed_obj)
        changed_obj['update_reason'] = 'updated'

        compare_traits = ed_traits_comp.compare(old_lgo_traits)
        old_lgo_traits = old_lgo_traits.reset_index(level=0)
        changed_traits = old_lgo_traits[old_lgo_traits.criterion_id.isin(compare_traits.index.values.tolist())]
        changed_traits = pd.DataFrame(changed_traits)
        changed_traits['update_reason'] = 'updated'

        changed_id_list = changed_goals.criterion_id.values.tolist() + changed_obj.criterion_id.values.tolist() + changed_traits.criterion_id.values.tolist()
        archive_id_list += changed_id_list
        archive_ids = ','.join(str(e) for e in archive_id_list)

        draft_new_goals = pd.concat([new_lgo_goals, changed_goals])
        draft_new_obj = pd.concat([new_lgo_obj, changed_obj])
        draft_new_traits = pd.concat([new_lgo_traits, changed_traits])

        new_goals = pd.DataFrame(draft_new_goals, columns=lgo_goals.columns.tolist()+['update_reason'])
        new_obj = pd.DataFrame(draft_new_obj, columns=lgo_obj.columns.tolist()+['update_reason'])
        new_traits = pd.DataFrame(draft_new_traits, columns=lgo_traits.columns.tolist()+['update_reason'])

        new_goals['created_at'] = dttm
        new_obj['created_at'] = dttm
        new_traits['created_at'] = dttm

        if len(archive_ids)>0:
            archiveRows(archive_ids, 'sat_criterion', 'criterion_id', dttm=dttm)

        if new_goals.shape[0]>0:
            insertIntoTable(new_goals, 'sat_criterion')
        if new_obj.shape[0]>0:
            insertIntoTable(new_obj, 'sat_criterion')
        if new_traits.shape[0]>0:
            insertIntoTable(new_traits, 'sat_criterion')

    def updateTable(table, raw_df, columns_dict={}, common_id = False, amount = 1000, nohub=False, ready=False, cursor=cursor, conn=conn, dttm=dttm):
        if not ready:
            df = pd.DataFrame(raw_df, columns=list(columns_dict.keys()), dtype=None, copy=None)
            df = df.rename(columns=columns_dict)
        else: 
            df = raw_df.copy()
        #print(df)
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
                df_temp['created_at'] = dttm
                insertIntoTable(df_temp, f'hub_{table}')
            else:
                nd_id_list=df[index_name].values.tolist()
                new_id_list = []
                for element in nd_id_list:
                    if element not in ed_id_list:
                        new_id_list.append(element)
                new_df = df[df[index_name].isin(new_id_list)]
                new_df = pd.DataFrame(new_df, columns=[index_name])
                new_df['created_at'] = dttm
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
            df['created_at'] = dttm
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
        if table == 'sat_major':
            archive_id_list = changed_id_list
        else:
            archive_id_list += changed_id_list
        archive_ids = ','.join(str(e) for e in archive_id_list)

        draft_new = pd.concat([new_df, changed])
        #print('draft_new')
        #print(draft_new)

        new = pd.DataFrame(draft_new, columns=df.columns.tolist()+['update_reason'])

        new['created_at'] = dttm
        #print('new')
        #print(new)

        if len(archive_ids)>0:
            archiveRows(archive_ids, table, index_name, dttm=dttm)

        if new.shape[0]>0:
            insertIntoTable(new, table)

    def updateLink(table, raw_df, columns_dict, f_index_name, s_index_name, add_data=[], f_common_id=False, s_common_id=False, f_amount=1000, s_amount=1000, cursor=cursor, conn=conn, dttm=dttm):
        #print(raw_df)
        df = pd.DataFrame(raw_df, columns=list(columns_dict.keys()), dtype=None, copy=True)
        df = df.rename(columns=columns_dict)
        index_name=table+'_id'
        
        if not f_common_id:
            df[f_index_name] += major_id * f_amount
        if not s_common_id:
            df[s_index_name] += major_id * s_amount

        cursor.execute(f'SELECT coalesce(max({index_name}),0)::integer FROM public.lnk_{table}')
        edata = cursor.fetchall()
        ed_cols = []
        for col in cursor.description:
            ed_cols.append(col[0])
        ed = pd.DataFrame(data=edata,columns=ed_cols)
        #print(ed)
        #print(ed.iloc[0,0])
        #print(int(ed.iloc[0,0]))
        start_index = ed.iloc[0,0] + 1
        f_filt = '1=1' if f_common_id else f'lnk.{f_index_name} >= {str(major_id*f_amount)} and lnk.{f_index_name} < {str((major_id+1)*f_amount)}'
        s_filt = '1=1' if s_common_id else f'lnk.{s_index_name} >= {str(major_id*s_amount)} and lnk.{s_index_name} < {str((major_id+1)*s_amount)}'
        if f_index_name == 'major_id':
            f_filt = f'lnk.{f_index_name} = {str(major_id)}'
        if s_index_name == 'major_id':
            s_filt = f'lnk.{s_index_name} = {str(major_id)}'
        cursor.execute(f'SELECT lnk.{f_index_name}::integer as {f_index_name}, lnk.{s_index_name}::integer as {s_index_name} FROM public.lnk_{table} as lnk JOIN public.sat_{table} as sat using ({index_name}) WHERE sat.updated_at is null and {f_filt} and {s_filt}')
        edata = cursor.fetchall()
        ed_cols = []
        for col in cursor.description:
            ed_cols.append(col[0])
        ed = pd.DataFrame(data=edata,columns=ed_cols)
        ed_id_list = ed[f_index_name].values.tolist()
        #print(ed_id_list)
        #print(df)

        if ed_id_list==[]:
            df['created_at'] = dttm
            df.insert(0, index_name, range(start_index, start_index + len(df)))
            df_lnk = df.drop(columns=add_data)
            insertIntoTable(df_lnk, f'lnk_{table}')
            df['update_reason'] = 'created'
            df.drop(columns=[f_index_name, s_index_name], inplace=True)
            insertIntoTable(df, f'sat_{table}')
            return 1
        
        nd_id_list_f = df[f_index_name].values.tolist()
        nd_id_list_s = df[s_index_name].values.tolist()
        ed_id_list_f = ed[f_index_name].values.tolist()
        ed_id_list_s = ed[s_index_name].values.tolist()
        nd_zip = list(zip(nd_id_list_f , nd_id_list_s))
        ed_zip = list(zip(ed_id_list_f , ed_id_list_s))
        #print('nd_zip')
        #print(nd_zip)
        #print('ed_zip')
        #print(ed_zip)

        archive_id_list = []
        for element in ed_zip:
            if element not in nd_zip:
                archive_id_list.append(element)
        #print('archive_id_list')
        #print(archive_id_list)

        new_id_list = []
        for element in nd_zip:
            if element not in ed_zip:
                new_id_list.append(element)
        #print('new_id_list')
        #print(new_id_list)

        if archive_id_list != []:
            #archive_f, archive_s = zip(*archive_id_list)
            #archive_f_ids = ','.join(str(e) for e in list(archive_f))
            #archive_s_ids = ','.join(str(e) for e in list(archive_s))
            ##print('archive_f_ids')
            ##print(archive_f_ids)
            ##print('archive_s_ids')
            ##print(archive_s_ids)
            archive_lists = []
            for archive_f_ids, archive_s_ids in archive_id_list:
                cursor.execute(f'SELECT lnk.{index_name}::integer as {index_name} FROM public.lnk_{table} as lnk JOIN public.sat_{table} as sat using ({index_name}) WHERE sat.updated_at is null and lnk.{f_index_name} in ({str(archive_f_ids)}) and lnk.{s_index_name} in ({str(archive_s_ids)})')
                edata = cursor.fetchall()
                ed_cols = []
                for col in cursor.description:
                    ed_cols.append(col[0])
                archive_list = pd.DataFrame(data=edata,columns=ed_cols)
                archive_lists.append(archive_list)
            archive_list = pd.concat(archive_lists)
            archive_id_list = archive_list[index_name].values.tolist()
            #print('archive_id_list')
            #print(archive_id_list)
            archive_ids = ','.join(str(e) for e in archive_id_list)
            if len(archive_ids)>0:
                archiveRows(archive_ids, f'sat_{table}', index_name, dttm=dttm)
        #print(new_id_list)
        if new_id_list != []:
            new_f, new_s = zip(*new_id_list)
            #print(list(new_f))
            new_df = df[(df[f_index_name].isin(list(new_f))) & (df[s_index_name].isin(list(new_s)))]
            new_df = pd.DataFrame(new_df)
            new_df['created_at'] = dttm
            new_df.insert(0, index_name, range(start_index, start_index + len(new_df)))
            new_df_sat = new_df.drop(columns=[f_index_name, s_index_name])
            new_df_sat['update_reason'] = 'created'
            new_df_lnk = new_df.drop(columns=add_data)
            #print('new_df')
            #print(new_df)
            #print('new_df_sat')
            #print(new_df_sat)
            insertIntoTable(new_df_sat, f'sat_{table}')
            insertIntoTable(new_df_lnk, f'lnk_{table}')
        
        if add_data == []:
            return 1
        else:
            match_id_list = []
            for element in nd_zip:
                if element in ed_zip:
                    match_id_list.append(element)
            if match_id_list != []:
                match_f, match_s = zip(*match_id_list)
                match_f_ids = ','.join(str(e) for e in list(match_f))
                match_s_ids = ','.join(str(e) for e in list(match_s))
            add_data_query_str = ''
            for col in add_data:
                add_data_query_str += f', sat.{col} as {col}'
            cursor.execute(f'SELECT lnk.{index_name}::integer as {index_name}, lnk.{f_index_name}::integer as {f_index_name}, lnk.{s_index_name}::integer as {s_index_name}{add_data_query_str} FROM public.lnk_{table} as lnk JOIN public.sat_{table} as sat using ({index_name}) WHERE sat.updated_at is null and lnk.{f_index_name} in ({match_f_ids}) and lnk.{s_index_name} in ({match_s_ids})')
            edata = cursor.fetchall()
            ed_cols = []
            for col in cursor.description:
                ed_cols.append(col[0])
            matches = pd.DataFrame(data=edata,columns=ed_cols)
            comparison = df.set_index([f_index_name,s_index_name]).join(matches.set_index([f_index_name,s_index_name]), how='inner', lsuffix='', rsuffix='_new')
            comparison = comparison.reset_index()
            comparison = comparison[comparison.columns.drop([f_index_name, s_index_name] + list(comparison.filter(regex='_new$')))]
            #print('comparison')
            #print(comparison)
            updateTable(table, comparison, nohub=True, ready=True, common_id = True, dttm=dttm)

    updateTable('artifact', artifact, {"ArtifactID": "artifact_id", "Наименование замера": "artifact_name"}, dttm=dttm)
    updateLink('course_artifact', artifact, {"ArtifactID": "artifact_id", "CourseID": "course_id"}, 'artifact_id', 'course_id', dttm=dttm)
    updateLink('artifact_criterion', lgo, {"ArtifactID": "artifact_id", "TraitID": "criterion_id"}, 'artifact_id', 'criterion_id', dttm=dttm)

    #updateTable('student', student, {"student_id": "student_id"}, common_id=True, dttm=dttm)
    updateLink('student_major', student, {"student_id": "student_id", "major_id": "major_id"}, 'student_id', 'major_id', f_common_id=True, s_common_id=True, dttm=dttm)

    updateTable('major', major_df, {'major_id': 'major_id', 'degree': 'degree', 'program_name': 'program_name', 'major_name': 'major_name'}, common_id=True, dttm=dttm)
    
    updateTable('course', courses_df, {'Semester': 'semester', 'Course name': 'course_name', 'CourseID': 'course_id', 'Course status (core/elective)': 'is_elective', 'Elective pack code (troughout)': 'elective_pack_code'}, dttm=dttm)
    updateLink('course_criterion', courses_obj, {"CourseID": "course_id", "level_1": "criterion_id", 0: 'value'}, 'course_id', 'criterion_id', add_data=['value'], dttm=dttm)

    courses_obj = courses_obj.drop(columns=["level_1", 0]).drop_duplicates()
    courses_obj['major_id'] = major_id

    updateLink('major_course', courses_obj, {"CourseID": "course_id", "major_id": "major_id"}, 'course_id', 'major_id', s_common_id = True, dttm=dttm)


    cursor.close()
    conn.close()