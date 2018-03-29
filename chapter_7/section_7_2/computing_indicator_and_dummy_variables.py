import numpy as np
import pandas as pd

# TO-DO

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})

# 虚拟变量
pd.get_dummies(df['key'])
