import pandas as pd

df = pd.read_csv('data/stock_px.csv', parse_dates=True, index_col=0)

close_px = df[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()

close_px.AAPL.plot()
