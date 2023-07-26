import time

from data import BUYSELL
from stock import Stock

class Trade(object):
    def __init__(self, stockSymbol, quantity, buySell, price):
        self.stock = Stock(stockSymbol) 
        self.timeStamp = time.time()
        self.quantity = quantity
        self.buySell = buySell
        assert self.buySell in [BUYSELL.BUY.value, BUYSELL.SELL.value]
        self.price = price

def main():
    trade = Trade('ALE', 10, BUYSELL.BUY.value, 3.14)
