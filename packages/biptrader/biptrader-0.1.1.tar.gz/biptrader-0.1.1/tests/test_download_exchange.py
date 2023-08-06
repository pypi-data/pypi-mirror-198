from datetime import datetime, date, timedelta
from unittest import TestCase
import pytz
from biptrader.download_exchange import DownloadExchange,DownloadExchangeDB
from biptrader.my_exchange import MyKucoin
from biptrader import util


class TestDownload(TestCase):

    def __init__(self):
        self.props = util.load_properties_dict('test-config.properties')
        exchange = MyKucoin({
            'adjustForTimeDifference': True,
            "apiKey": self.props["API_KEY"],
            "secret": self.props["API_SECRET"],
            'password': self.props["API_PASSPHRASE"],
        })
        self.d = DownloadExchange(exchange,"data/")

    def test_download(self):
        self.d.download(self.props["CCXT_TICKER_NAME"],timeframe="5m",since=datetime(2022,4,1,tzinfo=pytz.utc).timestamp()*1000,limit=DownloadExchange.DAY_5M_LIMIT)
        self.d.download(self.props["CCXT_TICKER_NAME"],timeframe="5m",since=datetime(2022,4,2,tzinfo=pytz.utc).timestamp()*1000,limit=DownloadExchange.DAY_5M_LIMIT)

    def test_download_day(self):
        # self.d.download_day(2022,4,3,self.props["CCXT_TICKER_NAME"])
        self.d.download_day(2022,1,2,self.props["CCXT_TICKER_NAME"])

    def test_download_month(self):
        self.d.download_month(2022,1,self.props["CCXT_TICKER_NAME"])
        # self.d.download_month(2022,4,self.props["CCXT_TICKER_NAME"])
        # self.d.download_month(2022,3,self.props["CCXT_TICKER_NAME"])

    def test_download_year(self):
        self.d.download_year(2022,self.props["CCXT_TICKER_NAME"])
        # self.d.download_month(2022,3,self.props["CCXT_TICKER_NAME"])

    def test_download_start_end(self):
        self.d.download_start_end(start=date(2021,1,1),end=date(2021,12,31),symbol=self.props["CCXT_TICKER_NAME"])

    def test_datetime(self):
        print(  datetime.fromtimestamp(1641081600000.0/1000) )
        print(  datetime.fromtimestamp(1641081600000.0/1000).strftime("%Y%m%d_%H%M%S") )
        print(  datetime(2022,1,2).timestamp() )
        print(  datetime(2022,1,2) )
        print(  datetime(2022,1,2).strftime("%Y%m%d") )

    def test_loop_start_end(self):
        start=date(2022,1,2)
        end=date(2022,3,3)
        for n in range(int((end-start).days)):
            d = start + timedelta(n)
            print(d)


class TestDownloadDB(TestCase):
    def __init__(self):
        self.props = util.load_properties_dict('test-config.properties')
        exchange = MyKucoin({
            'adjustForTimeDifference': True,
            "apiKey": self.props["API_KEY"],
            "secret": self.props["API_SECRET"],
            'password': self.props["API_PASSPHRASE"],
        })
        d = DownloadExchangeDB(exchange,'sqlite:///../data/candle.db',"../data")

    def test_download(self):
        self.d.download(self.props["CCXT_TICKER_NAME"],timeframe="5m",since=datetime(2022,4,1,tzinfo=pytz.utc).timestamp()*1000,limit=DownloadExchangeDB.DAY_5M_LIMIT)
        self.d.download(self.props["CCXT_TICKER_NAME"],timeframe="5m",since=datetime(2022,4,2,tzinfo=pytz.utc).timestamp()*1000,limit=DownloadExchangeDB.DAY_5M_LIMIT)

    def test_download_day(self):
        # self.d.download_day(2022,1,2,self.props["CCXT_TICKER_NAME"])
        self.d.download_day(2022,4,22,self.props["CCXT_TICKER_NAME"])

    def test_download_month(self):
        self.d.download_month(2022,1,self.props["CCXT_TICKER_NAME"])
        # self.d.download_month(2022,4,self.props["CCXT_TICKER_NAME"])
        # self.d.download_month(2022,3,self.props["CCXT_TICKER_NAME"])

    def test_download_year(self):
        self.d.download_year(2022,self.props["CCXT_TICKER_NAME"])
        # self.d.download_month(2022,3,self.props["CCXT_TICKER_NAME"])

    def test_download_start_end(self):
        self.d.download_start_end(start=date(2021,1,1),end=date(2021,12,31),symbol=self.props["CCXT_TICKER_NAME"])

# class TestDownloadExchangeDB(TestCase):
#     def test_download_day(self):
#         self.fail()
