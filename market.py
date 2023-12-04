

"""
what does first version of a market needs to have


    securities
    traders

"""
class trader:
    def __int__(self, budget,portfolio=None):
        self.budget = budget
        self.portfolio = portfolio if portfolio else {}

    def buy(self, sec,limit=None,expiration=None):


class security:


    pass

class order:

    def __init__(self,trader,price,type,ammount):
        self.owner=trader
        self.price=price
        self.type=type
        self.ammount=ammount


class market:
    def __init__(self):
        self.traders = []
        self.sell_orders = []
        self.buy_orders = []
        self.securites = []
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
    def proccess_orders(self,sell_order,buy_order,ammount):
        sec = sell_order.type
        buyer = buy_order.owner
        seller = sell_order.owner

        # Remove exact securities from the portfolio of the seller
        seller_portfolio = seller.portfolio

        if sec in seller_portfolio:
            # Check if the seller has enough of the securities to sell
            if seller_portfolio[sec] >= ammount:
                # Remove the sold securities from the seller's portfolio
                seller_portfolio[sec] -= ammount
            else:
                # If the seller doesn't have enough securities, raise an exception or handle it as needed
                raise ValueError("Seller doesn't have enough securities to sell")

            # Add the bought securities to the buyer's portfolio
            buyer.portfolio[sec] = buyer.portfolio.get(sec, 0) + ammount
            seller.portfolio[sec] = seller.portfolio.get(sec, 0) - ammount
            # Perform any other necessary processing/logic based on the successful transaction
            # ...

            # Assuming you may want to return some information about the transaction
            return f"Transaction successful: Sold {ammount} {sec} from {seller.name} to {buyer.name}"

        else:
            # If the seller doesn't have the specified securities, raise an exception or handle it as needed
            raise ValueError(f"Seller doesn't have {sec} securities to sell")
    def match_orders(self):
        for s in self.sell_orders:
            for b in self.buy_orders:
                if s.price==b.price:
                    pass
                    # complete the order


