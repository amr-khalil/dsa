"""
What is the bridge pattern?
The Bridge design pattern is used to separate an abstraction from its implementation, 
allowing the two to vary independently.
This is especially useful for large systems, such as those used by Amazon, 
where you may have different services that require different ways of processing data. 
Here is an example in Python using the Bridge design pattern. Let's assume a scenario where we are building an e-commerce system with multiple payment methods and order types.


When to use the bridge pattern?
You can use the bridge pattern if you want to:
- extend a class in several independent dimensions
- change the implementation at run time
- share the implementation between objects


Bridge Design Pattern Example in Python
Payment Method Abstraction: Defines the abstraction for the payment methods.
Concrete Payment Implementations: Specific payment methods like PayPal and CreditCard.
Order Type Abstraction: Defines the abstraction for different order types.
Concrete Order Implementations: Specific order types like physical and digital products.
"""

from abc import ABC, abstractmethod

######Payment########
# Payment Method Abstraction
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Concrete Payment Implementations
class PayPal(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal.")

class CreditCard(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using Credit Card.")

######Oder########
# Order Type Abstraction
class Order(ABC):
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    @abstractmethod
    def process_order(self, amount: float):
        pass

# Concrete Order Implementations
class PhysicalOrder(Order):
    def process_order(self, amount: float):
        print("Processing Physical Order")
        self.payment_method.pay(amount)

class DigitalOrder(Order):
    def process_order(self, amount: float):
        print("Processing Digital Order")
        self.payment_method.pay(amount)

class SubscriptionOrder(Order):
    def process_order(self, amount: float):
        print("Processing Subscription Order")
        self.payment_method.pay(amount)


# Usage Example
if __name__ == "__main__":
    # Using PayPal for a Physical Order
    paypal = PayPal()
    physical_order = PhysicalOrder(paypal)
    physical_order.process_order(99.99)

    # Using Credit Card for a Digital Order
    credit_card = CreditCard()
    digital_order = DigitalOrder(credit_card)
    digital_order.process_order(29.99)

    # Using PayPal for a Subscription Order
    subscription_order = SubscriptionOrder(paypal)
    subscription_order.process_order(9.99)