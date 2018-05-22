import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
transform = lambda x: x[:4].upper()
data.index = data.index.map(transform)

data.rename(index=str.title, columns=str.upper)

data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'})

data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'},
            inplace=True)
