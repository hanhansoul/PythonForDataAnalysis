import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])
grouped.mean()

means = df['data1'].groupby([df['key1'], df['key2']]).mean()

means = df.groupby(['key1', 'key2']).mean()

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
for k, v in df['data1'].groupby([states, years]):
    print(k)
    print(v)
df['data1'].groupby([states, years]).mean()

# iterating over groups

for name, group in df.groupby('key1'):
    print(name)
    print(group)

pieces = dict(list(df.groupby('key1')))


# selecting a column or subset of columns
def output(d):
    for k, v in d:
        print(k)
        print(v)


g1 = df.groupby('key1')['data1']
g2 = df.groupby('key1')[['data1']]

# g1返回的是一个或多个Series
output(g1)
# g2返回的是一个或多个DataFrame，还可以指定多列
output(g2)

g3 = df.groupby(['key1', 'key2'])['data1']
g4 = df.groupby(['key1', 'key2'])[['data1', 'data2']]
output(g3)
output(g4)

# g1返回的是一个或多个Series
output(g1)
# g2返回的是一个或多个DataFrame，还可以指定多列
output(g2)

# axis=1
print(df.dtypes)
for dtype, group in df.groupby(df.dtypes, axis=1):
    print(dtype)
    print(group)

# group with dicts and series
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
# iloc[行索引, 列索引]
people.iloc[2:3, [1, 2]] = np.nan
print(people)

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}

by_columns = people.groupby(mapping, axis=1)

map_series = pd.Series(mapping)
people.groupby(map_series, axis=1)
