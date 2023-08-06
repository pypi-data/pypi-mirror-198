""" download_exchange :
    4/13/2022 2:30 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import calendar
from datetime import datetime, date, timedelta

import pandas as pd
from os.path import exists

import pytz
from ccxt import Exchange
# from pip._internal.cli.progress_bars import DownloadBar
from sqlalchemy import create_engine

# from biptrader.common import config

class DownloadExchange:
    DAY_1M_LIMIT=1440
    DAY_5M_LIMIT=288
    DAY_15M_LIMIT=96
    DAY_30M_LIMIT=48

    exchange=None
    cache_path= "../data"

    def __init__(self,exchange,cache_path="."):
        self.exchange = exchange
        self.cache_path = cache_path

    def download(self, symbol, since, limit, timeframe='5m', params = {'partial': False},tzinfo=pytz.utc):
        file_path = f"{self.cache_path}/{self.exchange.name}_{symbol.replace('/','-')}_{timeframe}_{self.__get_since_str(since,tzinfo)}_{limit}.csv"

        if exists(file_path):
            # pd.read_csv(name,header=0,index_col=0,parse_dates=True)
            ticker_df = pd.read_csv(file_path,header=0,parse_dates=True)
            return ticker_df
        else:
            try:
                data = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=limit, params=params)
            except Exception as ex:
                print(f"{datetime.now(pytz.utc)} Error in fetching data for:{file_path}",ex)
                raise ex

            if data is not None and len(data)==limit:
                ticker_df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'vol'])
                ticker_df['date'] = pd.to_datetime(ticker_df['timestamp'], unit='ms')
                ticker_df['symbol'] = symbol
                ticker_df.to_csv(file_path)
                return ticker_df
            else:
                msg = f"{datetime.now(pytz.utc)} Error incomplete received data for {file_path}! len={len(data)}!={limit}"
                print(msg)
                raise Exception(msg)

        return None


    def __get_since_str(self,since,tzinfo=pytz.utc):
        since_date = datetime.fromtimestamp(since/1000,tzinfo)
        since_date_str = since_date.strftime("%Y%m%d")
        if since_date.hour!=0 or since_date.minute!=0 or since_date.second!=0 :
            since_date_str = since_date.strftime("%Y%m%d_%H%M%S")
        return since_date_str

    def get_day_limit_of_timeframe(self, timeframe):
        return int((24*60*60) / Exchange.parse_timeframe(timeframe))

    def download_day(self, year, month, day, symbol, timeframe='5m',tzinfo=pytz.utc):
        return self.download(symbol, timeframe=timeframe, since=datetime(year,month,day ,tzinfo=tzinfo).timestamp()*1000
                             , limit=self.get_day_limit_of_timeframe(timeframe), tzinfo=tzinfo)

    def download_date(self, date, symbol, timeframe='5m', tzinfo=pytz.utc):
        return self.download_day(date.year, date.month, date.day, symbol,timeframe=timeframe, tzinfo=tzinfo)

    def download_start_end(self, start, end, symbol, timeframe='5m', tzinfo=pytz.utc):
        df_list =[]
        today = date.today()
        for n in range(int((end-start).days)+1):
            d = start + timedelta(n)
            if date(d.year,d.month,d.day)<today :
                df = self.download_day(d.year, d.month, d.day, symbol,timeframe=timeframe, tzinfo=tzinfo)
                df_list.append(df)
            else:
                break
        return pd.concat(df_list, axis=0, ignore_index=True)


    def download_month(self, year, month, symbol, timeframe='5m', tzinfo=pytz.utc):
        return self.download_start_end(date(year,month,1),date(year,month,calendar.monthrange(year,month)[1])
                        ,symbol, timeframe, tzinfo)

    def download_year(self, year, symbol, timeframe='5m', tzinfo=pytz.utc):
        return self.download_start_end(date(year,1,1),date(year,12,31)
                                       ,symbol, timeframe, tzinfo)

class DownloadExchangeDB(DownloadExchange):
    table_prefix = 'dl_candle'
    sql_create_candle5m_table = f"create table if not exists {table_prefix}5m (id integer,platform text, symbol text, timestamp integer,date text" \
                                ",open real,low real,high real,close real,vol real)"

    def __init__(self,exchange,db_url,cache_path="."):
        super(DownloadExchangeDB, self).__init__(exchange, cache_path)
        self.db_url = db_url
        self.engine = create_engine(self.db_url)
        conn = self.engine.connect()
        conn.execute(self.sql_create_candle5m_table)
        conn.close()

    def download_day(self, year, month, day, symbol, timeframe='5m',tzinfo=pytz.utc):
        _date = date(year,month,day).strftime("%Y-%m-%d")
        _table=f"{self.table_prefix}{timeframe}"
        sql = f"select timestamp,open,high,low,close,vol,date,symbol from {_table} where substr(date,1,10)='{_date}'"
        df = pd.read_sql_query(sql,self.engine)
        if len(df)!=super(DownloadExchangeDB,self).get_day_limit_of_timeframe(timeframe):
            sql = f"delete from {_table} where substr(date,1,10)='{_date}'"
            self.engine.execute(sql)
            df = super(DownloadExchangeDB,self).download_day(year, month, day, symbol, timeframe,tzinfo)
            df['platform']='kucoin'
            if 'Unnamed: 0' in df.columns:
                del df['Unnamed: 0']
            df.index.name="id"
            df.to_sql(_table,self.engine, if_exists='append', index=True)

        return df

