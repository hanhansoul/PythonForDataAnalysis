import pandas as pd
import numpy as np


def output(d):
    for k, v in d:
        print(k)
        print(v)


tips = pd.read_csv("data/tips.csv")
tips['tip_pct'] = np.random.rand(244)
grouped = tips.groupby(['day', 'smoker'])

# 用聚合函数处理Series
# group之后分组生成多个Series
grouped_pct = grouped['tip_pct']
output(grouped_pct)
# 生成一个Series
grouped_pct.agg('mean')
# 生成给一个DataFrame，列名即给定的函数名
grouped_pct.agg(['mean', 'std', lambda x: x.max() - x.min()])
# 使用tuple可以指定结果DataFrame的列名
grouped_pct.agg(['mean', 'std', ('peak', lambda x: x.max() - x.min())])

# 用聚合函数处理DataFrame
functions = ['count', 'mean', 'max']
output(grouped['tip_pct', 'total_bill'])
result = grouped['tip_pct', 'total_bill'].agg(functions)
grouped.agg({'tip': np.max, 'size': 'sum'})
grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'], 'size': 'sum'})

# as_index
tips.groupby(['day', 'smoker'], as_index=False).mean()
