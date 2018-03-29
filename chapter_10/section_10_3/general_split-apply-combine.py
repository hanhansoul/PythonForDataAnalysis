import pandas as pd
import numpy as np


def output(d):
    for k, v in d:
        print(k)
        print(v)


tips = pd.read_csv("data/tips.csv")
tips['tip_pct'] = np.random.rand(244)
grouped = tips.groupby(['day', 'smoker'])


def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]


top(tips, n=6)

output(tips.groupby('smoker'))
tips.groupby('smoker').apply(top)

# quantile and bucket analysis
frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})

quartiles = pd.cut(frame.data1, 4)


def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}


grouped = frame.data2.groupby(quartiles)

grouped.apply(get_stats)

grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()
