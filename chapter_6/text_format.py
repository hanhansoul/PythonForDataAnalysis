'''
read_csv        ,分隔符
read_table      \t分隔符
read_fwf        固定场宽数据，无分隔符
read_clipboard
read_excel
read_hdf        hdf5文件
read_html       HTML文件中的table
read_json       JSON
read_msgpack    MessagePack二进制格式
read_pickle
read_sas        SAS数据集格式
read_sql        SQL查询
read_state      State文件格式
read_feather    Feather二进制文件格式

Indexing
数据类型推断和转换
大文件的数据遍历
脏数据
'''

import pandas as pd
import numpy as np

frame = pd.read_csv('chapter_6/ex1.csv')
print(frame)
frame = pd.read_table('chapter_6/ex1.csv', sep=',')
print(frame)

frame = pd.read_csv('chapter_6/ex2.csv', header=None)
print(frame)
frame = pd.read_csv('chapter_6/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
print(frame)
frame = pd.read_csv('chapter_6/ex2.csv', names=['a', 'b', 'c', 'd', 'message'], index_col='message')
print(frame)

parsed = pd.read_csv('chapter_6/ex3.csv', index_col=['key1', 'key2'])
print(parsed)
