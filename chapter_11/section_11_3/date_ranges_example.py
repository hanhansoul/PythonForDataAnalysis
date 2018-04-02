import pandas as pd

pd.date_range('2012-04-01', '2012-06-01')
pd.date_range(start='2012-04-01', periods=20)
pd.date_range(end='2012-06-01', periods=20)

pd.date_range('2000-01-01', '2000-12-01', freq='BM')
pd.date_range('2012-05-02 12:34:56', periods=5, normalize=True)
