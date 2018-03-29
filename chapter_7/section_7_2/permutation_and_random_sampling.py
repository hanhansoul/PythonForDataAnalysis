import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(5 * 4).reshape(5, 4))
sampler = np.random.permutation(5)

df.take(sampler)

df.sample(3)
