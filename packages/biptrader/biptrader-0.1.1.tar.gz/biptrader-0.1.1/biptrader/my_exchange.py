import ccxt
from jproperties import Properties

class MyKucoin(ccxt.kucoin):

    def describe(self):
        d = super().describe()
        d['urls']['api']['public']='https://api.kucoin.com'
        d['urls']['api']['private']='https://api.kucoin.com'
        return d
