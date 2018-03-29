import sys
import pandas as pd
import numpy as np

data = pd.read_csv('chapter_6/ex5.csv')
print(data)
data.to_csv('chapter_6/out.csv')
data.to_csv(sys.stdout, na_rep='NULL')
data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, columns=['a', 'b', 'c'])

dates = pd.date_range('1/1/2017', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv(sys.stdout)
