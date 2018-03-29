import pandas as pd

xlsx = pd.ExcelFile('test/all.xlsx')
alls = pd.DataFrame(pd.read_excel(xlsx, 'Sheet1'), columns=['姓名', 'sum'])
alls['sum'] = 0

files = []
for i in range(1, 7):
    xlsx = pd.ExcelFile('test/' + str(i) + '.xls')
    df = pd.DataFrame(pd.read_excel(xlsx, 'Sheet1'), columns=['姓名', 'sum'])
    # df['sum'] = 0
    ss = df['姓名']
    files.append(ss)

ll = []
for x in alls.iterrows():
    for y in files:
        if x[1]['姓名'] in y.values:
            x[1]['sum'] += 1
    ll.append([x[1]['姓名'], x[1]['sum']])



d = {}
index = 1
for i in alls['姓名']:
    d[i] = [0, index]
    index += 1

for item in files:
    for t in item['姓名']:
        if t in d:
            d[t][0] += 1

ll = []
for i in d.items():
    ll.append(i[1])

ll.sort(key=lambda x: x[1])
ls = [x[0] for x in ll]
data = pd.Series(ls)

write = pd.ExcelWriter('test/out.xlsx')
data.to_excel(write, 'Sheet1')
write.save()

data.to_excel('test/out.xlsx')

xlsx = pd.ExcelFile('test/all.xlsx')
alls = pd.DataFrame(pd.read_excel(xlsx, 'Sheet1'), columns=['姓名', 'sum'])
