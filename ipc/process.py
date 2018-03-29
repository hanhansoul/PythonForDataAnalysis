import pandas as pd
import numpy as np
import pymssql
import re
from functools import reduce

a320 = pd.read_csv('ipc/A320AIPC1.CSV', header=None, names=['pn', 'act', 'sn', 'chapter', 'category'])
a330 = pd.read_csv('ipc/A330AIPC1.CSV', header=None, names=['pn', 'act', 'sn', 'chapter', 'category'])
a350 = pd.read_csv('ipc/A350AIPC1.CSV', header=None, names=['pn', 'act', 'sn', 'chapter', 'category'])
# a350 = pd.read_csv('ipc/input.CSV', header=None, names=['pn', 'act', 'sn', 'chapter', 'category'])

b320 = a320.drop_duplicates(['pn']).sort_values(by='pn')
b330 = a330.drop_duplicates(['pn']).sort_values(by='pn')
b350 = a350.drop_duplicates(['pn']).sort_values(by='pn')

b320[b320['pn'] == '0-123-000700000']
b330[b330['pn'] == '0-123-000700000']


def process(s):
    arr = s.split('-')
    res = []
    for item in arr:
        if len(item) >= 2 or len(res[-1]) >= 2:
            res.append(item)
        else:
            res[-1] = res[-1] + item
        if (len(res) == 4) and (len(res[-1]) >= 2):
            break
    # if [filter(lambda x: len(x) < 2, res)]:
    if reduce(lambda x, y: x and len(y) >= 2, res, True):
        return '-'.join(res)
    else:
        return s


b320['chapter'] = b320['chapter'].map(process)
b330['chapter'] = b330['chapter'].map(process)
b350['chapter'] = b350['chapter'].map(process)

s = pd.concat([b320, b330, b350])

m = s.drop_duplicates(['pn'])
m['category'] = m['category'].map(lambda x: x[1:])

args = []
for x in m.values:
    args.append(tuple(x))

conn = pymssql.connect('172.18.80.182', 'sa', 'sa', 'amis-csc')
cursor = conn.cursor()

sql = "INSERT INTO IPC(PN, \
       ACT, SN, CHAPTER, CATEGORY) \
       VALUES (%s, %s, %s, %s, %s )"

try:
    cursor.executemany(sql, args)
except Exception as e:
    print(e)

cursor.close()
conn.commit()
conn.close()
