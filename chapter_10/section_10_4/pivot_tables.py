import pandas as pd

tips = pd.read_csv('D:/Workspace/PythonForDataAnalysis/data/tips.csv')

print(tips.pivot_table(index=['day', 'smoker']))
print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker'))
# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns=['smoker']))

# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'],
#                        columns='smoker', margins=True))
