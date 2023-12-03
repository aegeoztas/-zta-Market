

"""
what does first version of a market needs to have


    securities
    traders

"""
class trader:
    def __int__(self, budget):
        self.budget = budget

    def buy(self, sec,limit=None,expiration=None):

    pass

class security:


    pass

class order:
    def __init__(self,trader,price,type):
        self.owner=trader
        self.price=price
        self.type=type


class market:
    def __init__(self):
        self.traders
        self.sell_orders
        self.buy_orders
        self.securites
    def add_securitie(self,sec):
        self.securities.append(sec)
    def add_trader(self,trade):
        self.traders.append(trade)
    def add_order(self,order):
        if order.type == 'sell':
            self.sell_orders.append(order)
        elif order.type == 'buy':
            self.buy_orders.append(order)
        self.orders.append(order)

    def process_orders(self):
        for s in self.sell_orders:
            for b in self.buy_orders:
                if s.price==b.price:
                    pass
                    # complete the order

