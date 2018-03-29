import pandas as pd
import numpy as np


def output(d):
    for k, v in d:
        print(k)
        print(v)


s = pd.Series(np.random.randn(6))
s[::2] = np.nan
s.fillna(s.mean())

states = ['Ohio', 'New York', 'Vermont', 'Florida',+
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan

output(data.groupby(group_key))

fill_mean = lambda g: g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)

fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
data.groupby(group_key).apply(fill_func)
