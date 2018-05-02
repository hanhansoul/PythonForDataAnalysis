import pandas as pd

tips = pd.read_csv("data/tips.csv")
tips['tip_pct'] = tips['tip'] / tips['total_bill']
grouped = tips.groupby(['day', 'smoker'])

print(tips.pivot_table(index=['day', 'smoker']))  # 等同于 tips.groupby(['day', 'smoker']).mean()
print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker'))
print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True))

# len等同于count，计算每个分组中元素数量
print(tips.pivot_table('tip_pct', index=['time', 'smoker'], columns='day', aggfunc=len, margins=True))

print(tips.pivot_table('tip_pct', index=['time', 'size', 'smoker'], columns='day', aggfunc='mean',
                       margins=True, fill_value=0))

pt = tips.pivot_table('tip_pct', index=['time', 'size', 'smoker'], columns='day', aggfunc='mean',
                      margins=True, fill_value=0)

# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns=['smoker']))

# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'],
#                        columns='smoker', margins=True))
