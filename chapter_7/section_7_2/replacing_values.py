import pandas as pd
import numpy as np

# replace()

data = pd.Series([1., -999., 2., -999., -1000., 3.])
data.replace(-999, np.nan)
data.replace([-999, -1000], np.nan)
data.replace({-999: np.nan, -1000: 0})
