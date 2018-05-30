from datetime import datetime
import numpy as np
import pandas as pd

types = {
    '机号': str, '免表号': str, '合同号': str, '报关日期': str, '报关单号': str, '贸易方式': str, '报关金额': np.float64, '租金期间': str,
    '租金期数': str, '汇率': np.float64, '完税价格': np.float64, '关税率': np.float64, '关税': np.float64, '增值税率': np.float64,
    '增值税': np.float64, '填发时间': str, '税票交财务时间': str, '备注': str}

e = pd.read_excel('E:\development\PythonForDataAnalysis\merge_excel\input.xlsx',
                  sheet_name=1,
                  columns=['机号', '免表号', '合同号', '报关日期', '报关单号', '贸易方式', '报关金额', '租金期间', '租金期数',
                           '汇率', '完税价格', '关税率', '关税', '增值税率', '增值税', '填发时间', '税票交财务时间', '备注'],
                  dtype=types)

# dtype = [str, str, str, datetime, str, str, float16, str, int, float16, float16, float16,
#          float16, float16, float16, datetime, datetime, str]
print(e.keys())

print(e['B-1057租金'].count())
col = e['B-1057租金'].columns

res = pd.DataFrame(columns=col)
for k, v in e.items():
    if '机号' in v.columns and v['机号'].count() > 0:
        res = pd.concat([res, v])

out = pd.DataFrame(res, columns=col)
out = out.replace('nan', '')

out['报关日期'] = out['报关日期'].map(lambda x: x.split(' ')[0].replace('-', '/'))
out['填发时间'] = out['填发时间'].map(lambda x: x.split(' ')[0].replace('-', '/'))
out['税票交财务时间'] = out['税票交财务时间'].map(lambda x: x.split(' ')[0].replace('-', '/'))

writer = pd.ExcelWriter('E:\development\PythonForDataAnalysis\merge_excel\output.xlsx')
out.to_excel(writer, 'Sheet1')
writer.save()
