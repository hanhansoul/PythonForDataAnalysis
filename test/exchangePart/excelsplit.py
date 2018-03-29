records = {}

with open('excel_input', encoding='UTF-8') as f:
    for line in f:
        arr = line.split('\t')
        for x in [3, 7, 8]:
            pns = arr[x].split(',')
            for item in pns:
                if x == 3 or (item != '' and item not in records):
                    records[item] = line

with open('excel_output', 'w', encoding='UTF-8') as f:
    for key, value in records.items():
        f.write(key + '\t' + value)
