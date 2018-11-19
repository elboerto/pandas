import pandas as pd
start = pd.Timestamp('20170101', tz='Europe/Berlin')
end = pd.Timestamp('20180101', tz='Europe/Berlin')
index = pd.date_range(start, end, freq='15min')
data = [1 for x in range(len(index))]
series = pd.Series(index=index, data=data)
dataframe = pd.DataFrame(series)
timestamp = pd.Timestamp('201701011515', tz='Europe/Berlin')

# Working
series[timestamp]
dataframe.loc[timestamp]

# Errors
del series[timestamp]
dataframe.drop(timestamp)
series.drop(timestamp)