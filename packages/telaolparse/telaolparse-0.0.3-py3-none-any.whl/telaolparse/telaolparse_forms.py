import psycopg2
import pandas as pd
import numpy as np
import json
import requests
import datetime as dt
import base64

def encodeb64(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

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

def archiveRows(ids, table, dttm, index, cur=cursor, conn=conn):
    query = f"UPDATE {table} SET updated_at = '{dttm}' WHERE {index} in ({ids}) and updated_at is null"
    try:
        cur.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        return 1

def updateTable(table, raw_df, metadata, dttm, columns_dict={}, common_id = False, amount = 1000, nohub=False, ready=False, cursor=cursor, conn=conn):
    if not ready:
        df = pd.DataFrame(raw_df, columns=list(columns_dict.keys()), dtype=None, copy=None)
        df = df.rename(columns=columns_dict)
    else: 
        df = raw_df.copy()
    print(df)
    index_name = table+'_id'
    major_id = int(metadata['major_id'][0])
    if not common_id:
        df[index_name] += major_id * amount
    filt = '1=1' if common_id else f'{index_name} >= {str(major_id*amount)} and {index_name} < {str((major_id+1)*amount)}'
    if not nohub:
        print('hub_upd')
        cursor.execute(f'SELECT * FROM public.hub_{table} where {filt}')
        edata = cursor.fetchall()
        ed_cols = []
        for col in cursor.description:
            ed_cols.append(col[0])
        ed = pd.DataFrame(data=edata,columns=ed_cols)
        print(ed)
        ed_id_list = ed[index_name].values.tolist()
        if ed_id_list==[]:
            df_temp = pd.DataFrame(df, columns=[index_name])
            df_temp['created_at'] = dttm
            print(df_temp)
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
            print(new_df)
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
    print(ed)
    print(ed_id_list)
    print(df)

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
    print('new_df')
    print(new_df)

    old_df = df[df[index_name].isin(ed_id_list)]
    old_df = old_df.set_index(index_name).drop_duplicates()
    old_df.sort_index(inplace=True)
    print('old_df')
    print(old_df)

    ed = ed[ed[index_name].isin(old_df.index.values.tolist())]
    ed = ed.set_index(index_name)
    ed_comp = pd.DataFrame(ed, columns=list(old_df.columns), dtype=None, copy=None)
    ed_comp.sort_index(inplace=True)
    print('ed_comp')
    print(ed_comp)

    compare = ed_comp.compare(old_df)
    old_df = old_df.reset_index(level=0)
    changed = old_df[old_df[index_name].isin(compare.index.values.tolist())]
    changed = pd.DataFrame(changed)
    changed['update_reason'] = 'updated'
    print('changed')
    print(changed)

    changed_id_list = changed[index_name].values.tolist()
    archive_id_list += changed_id_list
    archive_ids = ','.join(str(e) for e in archive_id_list)

    draft_new = pd.concat([new_df, changed])
    print('draft_new')
    print(draft_new)

    new = pd.DataFrame(draft_new, columns=df.columns.tolist()+['update_reason'])

    new['created_at'] = dttm
    print('new')
    print(new)

    if len(archive_ids)>0:
        archiveRows(archive_ids, table, index_name, dttm)

    if new.shape[0]>0:
        insertIntoTable(new, table)

def updateLink(table, raw_df, s_index_names, common_ids, amounts, metadata, dttm, columns_dict={}, ready=False, add_data=[], cursor=cursor, conn=conn):
    if not ready:
        df = pd.DataFrame(raw_df, columns=list(columns_dict.keys()), dtype=None, copy=None)
        df = df.rename(columns=columns_dict)
    else: 
        df = raw_df.copy()
    index_name=table+'_id'
    major_id = int(metadata['major_id'][0])
    for s_index_name, common_id, amount in zip(s_index_names, common_ids, amounts):
        if not common_id:
            df[s_index_name] += major_id * amount

    cursor.execute(f'SELECT coalesce(max({index_name}),0)::integer FROM public.lnk_{table}')
    edata = cursor.fetchall()
    ed_cols = []
    for col in cursor.description:
        ed_cols.append(col[0])
    ed = pd.DataFrame(data=edata,columns=ed_cols)
    print(ed)
    print(ed.iloc[0,0])
    print(int(ed.iloc[0,0]))
    start_index = ed.iloc[0,0] + 1
    select = []
    filt = '1=1'
    for s_index_name in s_index_names:
        select.append(f'lnk.{s_index_name}::integer as {s_index_name}')
    select = 'select ' + ', '.join(select)
    for s_index_name, common_id, amount in zip(s_index_names, common_ids, amounts):
        if not common_id:
            filt += f' and lnk.{s_index_name} >= {str(major_id*amount)} and lnk.{s_index_name} < {str((major_id+1)*amount)}'
    cursor.execute(f'{select} FROM public.lnk_{table} as lnk JOIN public.sat_{table} as sat using ({index_name}) WHERE sat.updated_at is null and {filt}')
    edata = cursor.fetchall()
    ed_cols = []
    for col in cursor.description:
        ed_cols.append(col[0])
    ed = pd.DataFrame(data=edata,columns=ed_cols)
    ed_id_list = ed[s_index_names[0]].values.tolist()
    print(ed_id_list)
    print(df)

    if ed_id_list==[]:
        df['created_at'] = dttm
        df.insert(0, index_name, range(start_index, start_index + len(df)))
        df_lnk = df.drop(columns=add_data)
        insertIntoTable(df_lnk, f'lnk_{table}')
        df['update_reason'] = 'created'
        df.drop(columns=s_index_names, inplace=True)
        insertIntoTable(df, f'sat_{table}')
        return 1
    
    nd_id_lists = []
    ed_id_lists = []
    for s_index_name in s_index_names:
        nd_id_lists.append(df[s_index_name].values.tolist())
        ed_id_lists.append(ed[s_index_name].values.tolist())
    nd_zip = list(zip(*nd_id_lists))
    ed_zip = list(zip(*ed_id_lists))
    print('nd_zip')
    print(nd_zip)
    print('ed_zip')
    print(ed_zip)

    archive_id_list = []
    for element in ed_zip:
        if element not in nd_zip:
            archive_id_list.append(element)
    print('archive_id_list')
    print(archive_id_list)

    new_id_list = []
    for element in nd_zip:
        if element not in ed_zip:
            new_id_list.append(element)
    print('new_id_list')
    print(new_id_list)

    if archive_id_list != []:
        archive_lists = []
        for row in archive_id_list:
            filt = ''
            for field, filtvalue in zip(s_index_names, list(row)):
                filt +=  f' and lnk.{field} = {str(filtvalue)}'
            cursor.execute(f'SELECT lnk.{index_name}::integer as {index_name} FROM public.lnk_{table} as lnk JOIN public.sat_{table} as sat using ({index_name}) WHERE sat.updated_at is null{filt}')
            edata = cursor.fetchall()
            ed_cols = []
            for col in cursor.description:
                ed_cols.append(col[0])
            archive_list = pd.DataFrame(data=edata,columns=ed_cols)
            archive_lists.append(archive_list)
        archive_list = pd.concat(archive_lists)
        archive_id_list = archive_list[index_name].values.tolist()
        print('archive_id_list')
        print(archive_id_list)
        archive_ids = ','.join(str(e) for e in archive_id_list)
        if len(archive_ids)>0:
            archiveRows(archive_ids, f'sat_{table}', index_name, dttm)

    if new_id_list != []:
        row_index = 0
        data_dict = {}
        for row in new_id_list:
            data_dict[row_index] = list(row)
            row_index += 1
        new_df = pd.DataFrame.from_dict(data_dict, orient='index',
                    columns=s_index_names)
        new_df = new_df.set_index(s_index_names).join(df.set_index(s_index_names), how='inner', lsuffix='', rsuffix='_new')
        new_df = new_df.reset_index()
        new_df = pd.DataFrame(new_df)
        new_df['created_at'] = dttm
        new_df.insert(0, index_name, range(start_index, start_index + len(new_df)))
        new_df_sat = new_df.drop(columns=s_index_names)
        new_df_sat['update_reason'] = 'created'
        new_df_lnk = new_df.drop(columns=add_data)
        print('new_df')
        print(new_df)
        insertIntoTable(new_df_lnk, f'lnk_{table}')
        #print('new_df_sat')
        #print(new_df_sat)
        #insertIntoTable(new_df_sat, f'sat_{table}')
    
    if add_data == []:
        updateTable(table, comparison, metadata, dttm=dttm, ready=True, common_id=True)
    else:
        match_id_list = []
        for element in nd_zip:
            if element in ed_zip:
                match_id_list.append(element)
        print(match_id_list)
        select_add_data = ''
        for col in add_data:
            select_add_data += f', sat.{col} as {col}'
        match_parts = []
        for row in match_id_list:
            filt = ''
            select_indexes = [index_name]
            for field, filtvalue in zip(s_index_names, list(row)):
                filt +=  f' and lnk.{field} = {str(filtvalue)}'
                select_indexes.append(f'lnk.{field}::integer as {field}')
            select_ind = 'select ' + ', '.join(select_indexes)
            cursor.execute(f'{select_ind}{select_add_data} FROM public.lnk_{table} as lnk JOIN public.sat_{table} as sat using ({index_name}) WHERE sat.updated_at is null{filt}')
            edata = cursor.fetchall()
            ed_cols = []
            for col in cursor.description:
                ed_cols.append(col[0])
            match = pd.DataFrame(data=edata,columns=ed_cols)
            match_parts.append(match)
        try:
            matches = pd.concat(match_parts)
            comparison = df.set_index(s_index_names).join(matches.set_index(s_index_names), how='inner', lsuffix='', rsuffix='_new')
            comparison = comparison.reset_index()
            comparison = comparison[comparison.columns.drop(s_index_names + list(comparison.filter(regex='_new$')))]
            print('comparison')
            print(comparison)
            updateTable(table, comparison, metadata, dttm=dttm, ready=True, common_id=True)
        except:
            updateTable(table, df, metadata, dttm=dttm, ready=True, common_id=True)


def handler(event, context):
    print(event)
    print(event['body'])
    result = encodeb64(event['body'])
    result = result.split('Break:\nPage')
    print(result)
    new_result = []
    for part in result:
        print(part.encode('ascii'))
        new_part_draft = part.split('\n\n')
        print(new_part_draft)
        new_part_keys = []
        new_part_values = []
        for subpart in new_part_draft:
            print(subpart.encode('ascii'))
            if len(subpart)>0:
                subpart = subpart.replace('\n','').split(':')
                if subpart[0] == 'Select rated student':
                    student_id = subpart[-1][-7:-1]
                elif subpart[0] == 'program_id':
                    new_part_keys.append('major_id')
                    new_part_values.append([subpart[-1]])
                else:
                    new_part_keys.append(subpart[0])
                    new_part_values.append([subpart[-1]])
        new_part = dict(zip(new_part_keys, new_part_values))
        print(new_part)
        new_result.append(new_part)
    print('new_result')
    print(new_result)
    metadata = new_result.pop(0)
    print('metadata')
    print(metadata)
    #major_id = int(metadata['major_id'])
    #course_id = int(metadata['course_id'])
    #artifact_id = int(metadata['artifact_id'])
    try:
        dttm = metadata['created_at'][0]
        print(dttm)
    except:
        dttm = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        metadata['created_at'] = [dttm]
    dfs = []
    for student in new_result:
        print(student)
        df = pd.DataFrame.from_dict(student)
        dfs.append(df)
    students = pd.concat(dfs)
    print(students)
    students['student_id'] = int(student_id)
    students.set_index('student_id', inplace = True)
    students.columns.name = 'criterion_id'
    measurements = students.stack()
    measurements.name = 'grade'
    measurements = measurements.transform(lambda x: x.split('**')[1])
    measurements = measurements.replace("Doesn't meet.", 1)
    measurements = measurements.replace('Meets.', 2)
    measurements = measurements.replace('Exceeds.', 3)
    print(measurements)
    measurements = pd.to_numeric(measurements, errors='ignore')
    print(measurements)
    measurements = measurements.reset_index()
    print(measurements)
    #cols = students.columns.values.to_list()
    #new_cols = []
    #for col in cols:
    #    new_col = col.replace('.','')
    #    new_cols.append(new_col)
    #measurements = students.rename(columns=dict(zip(cols, new_cols)))
    for field in metadata:
        if field != 'created_at':
            measurements[field] = int(metadata[field][0]) 
            measurements[field] = pd.to_numeric(measurements[field], errors='raise')
        else:
            measurements[field] = metadata[field][0]
    measurements['student_id'] = pd.to_numeric(measurements['student_id'], errors='raise')
    measurements['criterion_id'] = measurements['criterion_id'].transform(lambda x: int(x[0]+x[2]+x[-1]))
    measurements['criterion_id'] = pd.to_numeric(measurements['criterion_id'], errors='raise')
    #measurements = measurements.rename(columns={'program_id': 'major_id'})
    print(measurements.dtypes)

    updateLink('measurement', measurements, ['student_id','major_id','course_id','artifact_id','criterion_id'], [True,True,False,False,False], [0,0,1000,1000,1000], metadata=metadata, dttm=dttm, ready=True, add_data=['grade'])   