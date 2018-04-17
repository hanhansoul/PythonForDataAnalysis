import numpy as np
import pandas as pd

values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
pd.unique(values)
pd.value_counts(values)

values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(['apple', 'orange'])
dim.take(values)
