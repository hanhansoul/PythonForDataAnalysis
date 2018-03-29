import pandas as pd
import numpy as np

pd.options.display.max_rows = 10
result = pd.read_csv('chapter_6/ex4.csv')
print(result)

pd.read_csv('chapter_6/ex4.csv', nrows=5)

chunker = pd.read_csv('chapter_6/ex4.csv', chunksize=1000)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)
print(tot[:10])
