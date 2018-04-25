import pandas as pd
import numpy as np

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
print(by_columns.sum())

map_series = pd.Series(mapping)
people.groupby(map_series, axis=1).count()
