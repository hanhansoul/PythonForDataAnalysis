import pandas as pd
import numpy as np

"""
Categirical可以提高groupby操作效率
"""

np.random.seed(12345)
draws = np.random.randn(1000)
print(draws[:5])
bins = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
bins.codes[:10]

bins = pd.Series(bins, name='quartile')
results = (pd.Series(draws).groupby(bins).agg(['count', 'min', 'max']).reset_index())
results['quartile']
