import pandas as pd
from lxml import objectify

tables = pd.read_html('chapter_6/fdic_failed_bank_list.html')
print(len(tables))
failures = tables[0]
print(failures.head())

close_timestamps = pd.to_datetime(failures['Closing Date'])
print(close_timestamps.dt.year.value_counts())

path = 'performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']
for ele in root.INDICATOR:
    ele_data = {}
    for child in ele.getchildren():
        if child.tag in skip_fields:
            continue
        ele_data[child.tag] = child.pyval
    data.append(ele_data)

print(data)

