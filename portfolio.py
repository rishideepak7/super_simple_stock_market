
import numpy as np
import time

from data import BUYSELL
from trade import Trade

class Portfolio(object):
    def __init__(self, trades):
        self.trades = trades

    def volWeightedStockPrice(self):
        """Calculate Volume Weighted Stock Price"""
        currentTs = time.time() 
        filterTrades = [trade for trade in self.trades if (currentTs-trade.timeStamp) < 15*60]
        vwsp = (sum([filterTrade.price*filterTrade.quantity for filterTrade in filterTrades]) / sum([filterTrade.quantity for filterTrade in filterTrades]))
        return vwsp


    def gbce(self):
        """Calculate GBCE"""
        return np.prod([trade.price for trade in self.trades]) ** (1/len(self.trades))

def main():
    trade1 = Trade('ALE', 10, BUYSELL.BUY.value, 3.14)
    trade2 = Trade('GIN', 20, BUYSELL.SELL.value, 3.15)
    trade3 = Trade('JOE', 30, BUYSELL.BUY.value, 3.16)
    portfolio = Portfolio((trade1, trade2, trade3))
    print(portfolio.volWeightedStockPrice())
    print(portfolio.gbce())
