import pandas as pd
import numpy as np

df = pd.DataFrame({'category': ['a'] * 4 + ['b'] * 4,
                   'data': np.random.randn(8),
                   'weights': np.random.rand(8)})
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
grouped.apply(get_wavg)
