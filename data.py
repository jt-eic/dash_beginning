import pandas_datareader.data as web
import datetime
start = datetime.datetime(2022,1,1)
end = datetime.datetime.now()

stock = "^DJI"

df = web.DataReader(stock, "stooq", start, end)

print(df.head)