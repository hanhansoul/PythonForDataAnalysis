import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(1000, 4))
data[(np.abs(data) > 3).any(1)]

data[np.abs(data) > 3] = np.sign(data) * 3

