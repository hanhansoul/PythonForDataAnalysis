import pandas as pd


def output(d):
    for k, v in d:
        print(k)
        print(v)


tips = pd.read_csv("data/tips.csv")
tips['tip_pct'] = tips['tip'] / tips['total_bill']
grouped = tips.groupby(['day', 'smoker'])


def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]


top(tips, n=6)

output(tips.groupby('smoker'))
tips.groupby('smoker').apply(top)
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')

result = tips.groupby('smoker')['tip_pct'].describe()
result.unstack()
