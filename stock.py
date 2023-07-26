
from data import getStockDataDf, StockAttr

class Stock(object):
    def __init__(self, stockSymbol):
        self.stockSymbol = stockSymbol
        self.stockDataDf = getStockDataDf()
        self.stockDict = self.stockDataDf[self.stockDataDf[StockAttr.STOCK_SYMBOL.value] == self.stockSymbol].to_dict(orient='records')[0]
        self.stockType = self.stockDict[StockAttr.TYPE.value]
        self.lastDividend = self.stockDict[StockAttr.LAST_DIVIDEND.value]
        self.fixedDividend = self.stockDict[StockAttr.FIXED_DIVIDEND.value]
        self.parValue = self.stockDict[StockAttr.PAR_VALUE.value]

    def dividendYield(self, price):
        """Calculate Dividend Yield"""
        if price == 0:
            raise ZeroDivisionError('Please input non zero value of price')
        elif self.stockType == 'Common':
            return self.lastDividend/price
        elif self.stockType == 'Preferred':
            return (self.fixedDividend*self.parValue)/price
        else:
            raise ValueError('Cannot handle Stock Type: {stockType}'.format(stockType = self.stockType))

    def peRatio(self, price):
        """Calculate PE Ratio"""
        if self.lastDividend == 0:
            raise ZeroDivisionError('Cannot calculate PE Ratio when dividend is zero')
        else:
            return price/self.lastDividend

def main():
    stock = Stock('ALE')
    price = 3.14
    print(stock.dividendYield(price))
    print(stock.peRatio(price))
    stock = Stock('GIN')
    price = 3.14
    print(stock.dividendYield(price))
    print(stock.peRatio(price))
