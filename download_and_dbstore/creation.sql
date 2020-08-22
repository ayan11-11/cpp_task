
CREATE TABLE IF NOT EXISTS bitmex_1d_data(
	timestamp DATETIME,
symbol VARCHAR,
open REAL,
high REAL,
low REAL,
close REAL,
trades REAL,
volume REAL,
vwap REAL,
lastSize REAL,
turnover REAL,
homeNotional REAL,
foreignNotional REAL
);

CREATE TABLE IF NOT EXISTS bitmex_1h_data(
	timestamp DATETIME,
symbol VARCHAR,
open REAL,
high REAL,
low REAL,
close REAL,
trades REAL,
volume REAL,
vwap REAL,
lastSize REAL,
turnover REAL,
homeNotional REAL,
foreignNotional REAL
);

CREATE TABLE IF NOT EXISTS bitmex_5m_data(
	timestamp DATETIME,
symbol VARCHAR,
open REAL,
high REAL,
low REAL,
close REAL,
trades REAL,
volume REAL,
vwap REAL,
lastSize REAL,
turnover REAL,
homeNotional REAL,
foreignNotional REAL
);

CREATE TABLE IF NOT EXISTS bitmex_1m_data(
	timestamp DATETIME,
symbol VARCHAR,
open REAL,
high REAL,
low REAL,
close REAL,
trades REAL,
volume REAL,
vwap REAL,
lastSize REAL,
turnover REAL,
homeNotional REAL,
foreignNotional REAL
);
