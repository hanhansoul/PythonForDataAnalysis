import numpy as np
import pandas as pd

obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj.index.is_unique)
print(obj['a'])

frame = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
# frame = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'c'])
print(frame.loc['b'])
