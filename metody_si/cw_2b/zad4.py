import pandas

data = pandas.read_csv('cw_2b\\EURUSD_15m_BID_wyczyszczony.csv', nrows=500)
data = data.drop('High', axis=1)
data = data.drop('Low', axis=1)

data['Open'] = data['Open'].fillna(0)

print(data.head(10))
