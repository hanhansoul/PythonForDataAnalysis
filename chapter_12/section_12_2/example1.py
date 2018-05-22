import pandas as pd
import numpy as np

df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
                   'value': np.arange(12.)})

g = df.groupby('key').value
df.groupby('key').mean()
print(g)

print(g.transform(lambda x: x.mean()))
print(g.transform('mean'))
print(g.transform(lambda x: x * 2))

