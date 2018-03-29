import pandas as pd
import numpy as np
import csv

f = open('chapter_6/ex6.csv')
reader = csv.reader(f)
for line in reader:
    print(line)

with open('chapter_6/ex6.csv') as f:
    lines = list(csv.reader(f))

header, values = lines[0], lines[1:]
print(header)
print(values)

data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)
