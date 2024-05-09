"""
Requirement collection
The following are the requirements that we have defined for the online stock brokerage system:
R1: The system should allow the user to easily trade in stocks (buy or sell the stocks).
R2: Users are allowed to have numerous watchlists consisting of different stock quotes.
R3: Users may own different lots of the same stock. This implies that the system should be able to distinguish between several lots of the same stock if a user has purchased the same stock more than once.
R4: Every time a trade order is carried out, the system should be able to notify users.
R5: The system should allow the user to order the stock trade of the types given below:
Market order: Buy or sell stocks at the current market price.
Limit order: Buy or sell stocks at the price set by the user.
Stop-loss order: Buy or sell stocks when they reach a certain price.
Stop-limit order: Buy or sell stocks with a restriction on the limit price (maximum price to be paid, minimum price to be received, etc).
R6: The system should allow the user to make deposits and withdrawals using checks, wire transfers, or electronic bank transfers.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

# Actors: User, Admin

class Person(ABC):
    def __init__(self, name: str):
        self.name = name
        self.email = ""
        self.phone = ""
        self.address = ""
        self.date_of_birth = None
        


class User(Person):
    def __init__(self, name: str):
        self.name = name
        self.watchlists = []
        self.portfolio = {}

    def buy_stock(self, stock: Stock, quantity: int, order_type: str):
        # Implement the logic for buying stocks
        print(f"{self.name} bought {quantity} shares of {stock.symbol} at {stock.price} each.")

    def sell_stock(self, stock: Stock, quantity: int, order_type: str):
        # Implement the logic for selling stocks
        print(f"{self.name} bought {quantity} shares of {stock.symbol} at {stock.price} each.")

    def add_to_watchlist(self, stock: Stock):
        self.watchlists.append(stock)

    def remove_from_watchlist(self, stock: Stock):
        self.watchlists.remove(stock)

    def notify_trade_order(self, order_type: str):
        # Implement the logic for notifying users about trade orders
        pass

    def deposit(self, amount: float, method: str):
        # Implement the logic for depositing funds
        print(f"{self.name} deposited {amount} using {method}.")

    def withdraw(self, amount: float, method: str):
        # Implement the logic for withdrawing funds
        pass
    
class FreeUser(User):
    def __init__(self, name: str):
        super().__init__(name)
        
    def reset_password(self, order_type: str):
        # Implement the logic for resetting passwords
        pass
    
class PremiumUser(User):
    def __init__(self, name: str):
        super().__init__(name)
        
    def get_rends(self, order_type: str):
        # Implement the logic for resetting passwords
        pass
    
class Admin(User):
    def __init__(self, name: str):
        super().__init__(name)

    def add_stock(self, stock: Stock):
        # Implement the logic for adding new stocks
        pass

    def update_stock_price(self, stock: Stock, price: float):
        # Implement the logic for updating stock prices
        pass

    def cancel_trade_order(self, order_id: int):
        # Implement the logic for canceling trade orders
        pass

    def reset_password(self, order_type: str):
        # Implement the logic for resetting passwords
        pass
    

# components: Stock, TradeOrder, Watchlist, Portfolio   
class Stock:
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self.price = price
        
class TradeOrder:
    def __init__(self, stock: Stock, quantity: int, order_type: str):
        self.stock = stock
        self.quantity = quantity
        self.order_type = order_type
        self.order_id = None
        
class Watchlist:
    def __init__(self):
        self.stocks = []
        
    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        
    def remove_stock(self, stock: Stock):
        self.stocks.remove(stock)
        
class Portfolio:
    def __init__(self):
        self.lots = {}
        
    def add_lot(self, stock: Stock, quantity: int):
        if stock in self.lots:
            self.lots[stock] += quantity
        else:
            self.lots[stock] = quantity
            
    def remove_lot(self, stock: Stock, quantity: int):
        if stock in self.lots:
            self.lots[stock] -= quantity
            if self.lots[stock] <= 0:
                del self.lots[stock]
                
    def get_lots(self):
        return self.lots
    

class Singleton(type):
    __instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
    
    
class BrokerApp(metaclass=Singleton):
    def __init__(self):
        self.users = []
        self.admins = []
        self.stocks = []
        self.trade_orders = []
        self.watchlists = []
        self.portfolios = []
        
    def add_user(self, user: User):
        self.users.append(user)
        
    def add_admin(self, admin: Admin):
        self.admins.append(admin)
        
    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        
    def add_trade_order(self, trade_order: TradeOrder):
        self.trade_orders.append(trade_order)
        
    def add_watchlist(self, watchlist: Watchlist):
        self.watchlists.append(watchlist)
        
    def add_portfolio(self, portfolio: Portfolio):
        self.portfolios.append(portfolio)
        
    def remove_user(self, user: User):
        self.users.remove(user)
        
    def remove_admin(self, admin: Admin):
        self.admins.remove(admin)
        
    def remove_stock(self, stock: Stock):
        self.stocks.remove(stock)
        
    def remove_trade_order(self, trade_order: TradeOrder):
        self.trade_orders.remove(trade_order)
        
    def remove_watchlist(self, watchlist: Watchlist):
        self.watchlists.remove(watchlist)
        
    def remove_portfolio(self, portfolio: Portfolio):
        self.portfolios.remove(portfolio)
        
    def get_users(self):
        return self.users
    
    def get_admins(self):
        return self.admins
    
    def get_stocks(self):
        return self.stocks
    
    def get_trade_orders(self):
        return self.trade_orders
    
    def get_watchlists(self):
        return self.watchlists
    
    def get_portfolios(self):
        return self.portfolios
    
    def notify_users(self, message: str):
        for user in self.users:
            # Implement the logic for notifying users
            pass

    def notify_admins(self, message: str):
        for admin in self.admins:
            # Implement the logic for notifying admins
            pass

    def process_trade_orders(self):
        for trade_order in self.trade_orders:
            # Implement the logic for processing trade orders
            pass

    def update_stock_prices(self):
        for stock in self.stocks:
            # Implement the logic for updating stock prices
            pass

    
    
if __name__ == "__main__":
    broker = BrokerApp()
    print(id(broker))
    
    broker2 = BrokerApp()
    print(id(broker2))
    