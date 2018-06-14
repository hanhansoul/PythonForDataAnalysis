import pymssql
import pandas as pd
import numpy as np

conn = pymssql.connect(host='172.18.8.241', port=1433, user='sa', password='Scaljw@2016', database='AMIS-CSC')

sql320 = "select date1, ac, sn_o, reporter, record from a320_fault_massages " + \
         "where sn_o is not null and sn_o != '' and sn_o != 'N/A' " + \
         "order by date1 desc"
sql330 = "select date1, ac, sn_o, reporter, record from a330_fault_massages " + \
         "where sn_o is not null and sn_o != '' and sn_o != 'N/A' " + \
         "order by date1 desc"
df320 = pd.read_sql(sql320, con=conn)
df330 = pd.read_sql(sql330, con=conn)
conn.close()

dfac = pd.concat([df320, df330]).reset_index(drop=True).sort_values(by=['date1'], ascending=False)
dfsql = dfac.drop('sn_o', axis=1).join(dfac['sn_o']
                                       .str.split(',', expand=True)
                                       .stack()
                                       .reset_index(level=1, drop=True)
                                       .rename('sn_o')
                                       .str.strip())
dfsql[dfsql == 'N/A'] = np.nan
dfsql.dropna(inplace=True)
dfsql = dfsql.sort_values(by=['date1'], ascending=False)
dfsql.drop_duplicates(subset='sn_o', inplace=True)

dfexcel = pd.read_excel('E:\\development\\PythonForDataAnalysis\\sql\\input2.xlsx', usecols=[3], dtype=str)

res = pd.merge(dfexcel, dfsql, left_on='序号', right_on='sn_o', how='left')
res = res.replace('nan', '')
# res['凭证日期'] = res['凭证日期'].map(lambda x: x.split(' ')[0].replace('-', '/'))
# res['证件日期'] = res['证件日期'].map(lambda x: x.split(' ')[0].replace('-', '/'))
# res['生产日期'] = res['生产日期'].map(lambda x: x.split(' ')[0].replace('-', '/'))
# res['到寿日期'] = res['到寿日期'].map(lambda x: x.split(' ')[0].replace('-', '/'))
res['date1'] = res['date1'].map(lambda x: x.strftime('%Y-%m-%d') if x is not pd.NaT else '')
# res['AMIS是否安装'] = (res['date1'] != '')

writer = pd.ExcelWriter('output2.xlsx')
res.to_excel(writer, index=False)
writer.save()
