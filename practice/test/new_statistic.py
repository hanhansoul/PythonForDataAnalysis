import pandas as pd

xlsx = pd.ExcelFile('test/all.xlsx')
alls = pd.read_excel(xlsx, 'Sheet1')

files = []
for i in range(1, 7):
    xlsx = pd.ExcelFile('test/' + str(i) + '.xls')
    files.append(pd.read_excel(xlsx, 'Sheet1'))

