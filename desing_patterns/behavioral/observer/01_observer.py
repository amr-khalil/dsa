"""
The Observer Design Pattern is a behavioral pattern that defines a one-to-many relationship between objects
so that when one object changes state, all its dependents are notified and updated automatically.


When to use the observer pattern?#
The observer pattern can be used to:
- To improve code management by breaking down large applications into a system of loosely-coupled objects
- provide greater flexibility by enabling a dynamic relationship between observers and subscribers which is otherwise not possible due to tight coupling
- improve communication between different parts of the application
- create a one-to-many dependency between objects that are loosely coupled
"""

# Subject (Observable)
class Inventory:
    def __init__(self):
        self._observers = []
        self._stock = {}

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, product_name, quantity):
        for observer in self._observers:
            observer.update(product_name, quantity)

    def add_product(self, product_name, quantity):
        if product_name in self._stock:
            self._stock[product_name] += quantity
        else:
            self._stock[product_name] = quantity
        self.notify_observers(product_name, quantity)

    def remove_product(self, product_name, quantity):
        if product_name in self._stock and self._stock[product_name] >= quantity:
            self._stock[product_name] -= quantity
            self.notify_observers(product_name, -quantity)

# Observer Interface
class User:
    def update(self, product_name, quantity):
        raise NotImplementedError("Subclasses must implement this method")

# Concrete Observers
class Customer(User):
    def __init__(self, name):
        self.name = name

    def update(self, product_name, quantity):
        action = "added to" if quantity > 0 else "removed from"
        print(f"[Customer] {self.name}: '{abs(quantity)}' units of '{product_name}' {action} inventory.")

class Vendor(User):
    def __init__(self, name):
        self.name = name

    def update(self, product_name, quantity):
        action = "added to" if quantity > 0 else "removed from"
        print(f"[Vendor] {self.name}: '{abs(quantity)}' units of '{product_name}' {action} inventory.")

# Example usage
if __name__ == "__main__":
    # Create an inventory
    amazon_inventory = Inventory()

    # Create users and subscribe to the inventory
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    vendor1 = Vendor("XYZ Vendor")

    amazon_inventory.add_observer(customer1)
    amazon_inventory.add_observer(customer2)
    amazon_inventory.add_observer(vendor1)

    # Update the inventory
    amazon_inventory.add_product("Laptop", 10)
    amazon_inventory.remove_product("Laptop", 5)
    amazon_inventory.add_product("Headphones", 50)
    amazon_inventory.remove_product("Headphones", 10)

    # Unsubscribe an observer
    amazon_inventory.remove_observer(customer2)

    # Further updates with a removed observer
    amazon_inventory.add_product("Smartphone", 30)
