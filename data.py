import pandas as pd

from enum import Enum

class StockAttr(Enum):
    STOCK_SYMBOL = 'Stock Symbol'
    TYPE = 'Type'
    LAST_DIVIDEND = 'Last Dividend'
    FIXED_DIVIDEND = 'Fixed Dividend'
    PAR_VALUE = 'Par Value'

class BUYSELL(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

STOCK_DATA = {
    StockAttr.STOCK_SYMBOL.value: ['TEA', 'POP', 'ALE', 'GIN', 'JOE'],
    StockAttr.TYPE.value: ['Common', 'Common', 'Common', 'Preferred', 'Common'],
    StockAttr.LAST_DIVIDEND.value: [0, 8, 23, 8, 13],
    StockAttr.FIXED_DIVIDEND.value: [None, None, None, 0.02, None],
    StockAttr.PAR_VALUE.value: [100, 100, 60, 100, 250],
    }

def getStockDataDf():
    return pd.DataFrame(STOCK_DATA)
