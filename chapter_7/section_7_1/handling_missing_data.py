import pandas as pd
import numpy as np

# dropna()
# fillna()
# isnull()
# notnull()

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data.isnull())

data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(data.dropna())
print(data[data.notnull()])

data = pd.DataFrame([[1., 6.3, 3.], [1., np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
print(data.dropna())
print(data.dropna(how='all'))

data[4] = np.nan
print(data.dropna(how='all', axis=1))

frame = pd.DataFrame(np.random.randn(7, 3))
# print(frame[:4])
# print(frame.iloc[:4, 1])
frame.iloc[:4, 1] = np.nan
frame.iloc[:2, 2] = np.nan
print(frame)
print(frame.dropna(thresh=2))

frame.fillna(0)
frame.fillna({1: 0.5, 2: 0})

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = np.NaN
df.iloc[4:, 2] = np.NaN

df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)

data = pd.Series([1., np.nan, 3.5, np.nan, 7])
data.fillna(data.mean())
