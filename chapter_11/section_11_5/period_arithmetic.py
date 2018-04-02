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

rng = pd.period_range('2006', '2009', freq='A-DEC')
pd.Series(np.random.randn(len(rng)), index=rng)

rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
pts = ts.to_period()