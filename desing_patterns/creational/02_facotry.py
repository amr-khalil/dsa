"""
The Factory Design Pattern is a creational pattern that provides a way to create objects while keeping the logic of instantiation separate.

The factory pattern is a creational pattern that provides a template that can be used to create objects. It is used in complex situations where the type of the object required varies and needs to be specified in each case.
It does not use the new keyword directly to instantiate objects. This means it does not explicitly require the use of a constructor to create objects. Instead, it provides a generic interface that delegates the object creation responsibility to the corresponding subclass.

When to use the factory pattern?
When the type of objects required cannot be anticipated beforehand
When multiple objects that share similar characteristics need to be created
When you want to generalize the object instantiation process since the object set up is complex in nature
"""


from abc import ABC, abstractmethod


class Order(ABC):
    """Abstract base class for Orders"""
    @abstractmethod
    def process_order(self):
        pass


class BookOrder(Order):
    """Concrete implementation for Book Orders"""
    def process_order(self):
        print("Processing Book Order: Packing books, printing book receipt...")


class ElectronicsOrder(Order):
    """Concrete implementation for Electronics Orders"""
    def process_order(self):
        print("Processing Electronics Order: Packing electronics, checking warranty details...")


class FurnitureOrder(Order):
    """Concrete implementation for Furniture Orders"""
    def process_order(self):
        print("Processing Furniture Order: Packing furniture, assembling installation guides...")


class OrderFactory:
    """Factory class to create Orders"""
    @staticmethod
    def create_order(order_type):
        if order_type == "book":
            return BookOrder()
        elif order_type == "electronics":
            return ElectronicsOrder()
        elif order_type == "furniture":
            return FurnitureOrder()
        else:
            raise ValueError(f"Unknown Order Type: {order_type}")


# Client code to demonstrate the use of Factory pattern
if __name__ == "__main__":
    # Create a Book Order
    book_order = OrderFactory.create_order("book")
    book_order.process_order()

    # Create an Electronics Order
    electronics_order = OrderFactory.create_order("electronics")
    electronics_order.process_order()

    # Create a Furniture Order
    furniture_order = OrderFactory.create_order("furniture")
    furniture_order.process_order()

    # Example of unknown type
    try:
        unknown_order = OrderFactory.create_order("clothing")
        unknown_order.process_order()
    except ValueErr