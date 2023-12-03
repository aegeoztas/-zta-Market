

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
        self.orders
        self.securites
    def add_securities(self,sec):
        self.securities.append(sec)
        self.