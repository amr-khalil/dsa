"""
What is the composite pattern?
The composite pattern is used to structure objects in a (tree-like hierarchy).
Here, each node of the tree can be composed of either child node(s) or be a leaf (no children objects).
This pattern allows the client to work with these components uniformly, that is, a single object can be treated exactly how a group of objects is treated.
This pattern allows the formation of deeply-nested structures.
If a leaf object receives the request sent by the client, it will handle it.
However, if the recipient is composed of children, the request is forwarded to the child components.

When to use the composite pattern?
- The composite pattern is powerful as it allows us to treat an object as a composite.
- Since both single and composite objects share the same interface, it allows reusing objects without worrying about their compatibility.
- You can use this pattern if you want to develop a scalable application that uses plenty of objects.
- It is particularly helpful in situations where you are dealing with a tree-like hierarchy of objects.
- An example of this pattern is being used by your operating system to create directories and subdirectories.
- Libraries like React and Vue also use this pattern to build reusable interfaces.
"""

from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_price(self):
        pass

class SingleProduct(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class ProductCollection(Product):
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.get_price()
        return total_price

# Client code
laptop = SingleProduct("Laptop", 1000)
mouse = SingleProduct("Mouse", 20)

electronics = ProductCollection("Electronics")
electronics.add_product(laptop)
electronics.add_product(mouse)

book = SingleProduct("Book", 15)
pen = SingleProduct("Pen", 2)

stationery = ProductCollection("Stationery")
stationery.add_product(book)
stationery.add_product(pen)

amazon_cart = ProductCollection("Amazon Cart")
amazon_cart.add_product(electronics)
amazon_cart.add_product(stationery)

# Calculate total price of the Amazon cart
total_price = amazon_cart.get_price()
print("Total price of the Amazon cart:", total_price)