import pandas as pd
import numpy as np
from datetime import datetime

p = pd.Period(2007, freq='A-DEC')
p + 5
p - 2

rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')

# frequency conversion

p = pd.Period('2007', freq='A-DEC')
p.asfreq('M', how='start')
p.asfreq('M', how='end')
