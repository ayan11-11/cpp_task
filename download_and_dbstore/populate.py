import csv, sqlite3, pandas

csvfile_1d="../script/XBTUSD-1d-data.csv"
csvfile_1h="../script/XBTUSD-1h-data.csv"
csvfile_5m="../script/XBTUSD-5m-data.csv"
csvfile_1m="../script/XBTUSD-1m-data.csv"

con = sqlite3.connect("bitmexData.db")

df = pandas.read_csv(csvfile_1d)
df.to_sql("bitmex_1d_data", con, if_exists='append', index=False)

df = pandas.read_csv(csvfile_1h)
df.to_sql("bitmex_1h_data", con, if_exists='append', index=False)

df = pandas.read_csv(csvfile_5m)
df.to_sql("bitmex_5m_data", con, if_exists='append', index=False)

df = pandas.read_csv(csvfile_1m)
df.to_sql("bitmex_1m_data", con, if_exists='append', index=False)

con.commit()
con.close()
