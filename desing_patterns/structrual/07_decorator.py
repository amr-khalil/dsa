"""
The decorator design pattern is useful for dynamically adding behavior to objects.
In Python, decorators can be implemented as functions or classes.
Here's a simple example of the decorator pattern applied to an Amazon-like context,
such as applying discounts and taxes to an order.

The decorator pattern focuses on adding properties,
functionalities, and behavior to existing classes dynamically.
The additional decoration functionalities aren’t considered essential enough to be a part of the original class definition as they can cause clutter.
Hence, the decorator pattern lets you modify the code without changing the original class.

Unlike the creational patterns, the decorator pattern is a structural pattern that does not focus on object creation rather decoration.
Hence, it doesn’t rely on prototypal inheritance alone; 
it takes the object and keeps adding decoration to it. This makes the process more streamlined.
Let’s take a look at an example to understand this concept better.

When to use the decorator pattern?
JavaScript developers can use the decorator pattern when they want to easily modify or extend the functionality of an object without changing its base code.
It can also be used if an application has a lot of distinct objects with the same underlying code. Instead of creating all of them using different subclasses, additional functionalities can be added to the objects using the decorator pattern.
A simple example is text formatting, where you need to apply different formattings such as bold, italics, and underline to the same text.

"""


class Order:
    def __init__(self, items):
        self.items = items

    def get_total(self):
        return sum(self.items)

    def __str__(self):
        return f"Order total: ${self.get_total():.2f}"


class OrderDecorator:
    def __init__(self, order):
        self.order = order

    def get_total(self):
        return self.order.get_total()

    def __str__(self):
        return str(self.order)


class DiscountDecorator(OrderDecorator):
    def __init__(self, order, discount_percent):
        super().__init__(order)
        self.discount_percent = discount_percent

    def get_total(self):
        return self.order.get_total() * (1 - self.discount_percent / 100)

    def __str__(self):
        return f"{super().__str__()} (After {self.discount_percent}% discount: ${self.get_total():.2f})"


class TaxDecorator(OrderDecorator):
    def __init__(self, order, tax_percent):
        super().__init__(order)
        self.tax_percent = tax_percent

    def get_total(self):
        return self.order.get_total() * (1 + self.tax_percent / 100)

    def __str__(self):
        return f"{super().__str__()} (After {self.tax_percent}% tax: ${self.get_total():.2f})"


if __name__ == '__main__':
    # Usage
    order = Order(items=[29.99, 9.99, 49.99])  # Example items
    print(order)  # Original Order

    # Applying a 10% discount
    discounted_order = DiscountDecorator(order, 10)
    print(discounted_order)

    # Applying a 5% tax on top of the discounted order
    taxed_order = TaxDecorator(discounted_order, 5)
    print(taxed_order)

    # Applying only a 5% tax on the original order without a discount
    tax_only_order = TaxDecorator(order, 5)
    print(tax_only_order)


