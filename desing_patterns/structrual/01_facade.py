"""
In English, the word facade means a deceptive front or appearance. Following this definition,
a facade pattern provides a simpler interface that hides the complex functionalities of a system.
This is widely used in JavaScript libraries like jQuery.

The facade pattern allows you to hide all the messy logic from the client and only display
the clear and easy-to-use interface to them. This allows them to interact with an API easily 
in a less error-prone way and without accessing the inner workings directly.

When to use the facade pattern?
The facade pattern is used to simplify a client’s interaction with a system.
So, it can be used when an application has a large and complex underlying code that the client does not need to see.
It can also be used when you want to interact with the methods present in a library
without knowing the processing that happens in the background.
An example can be of the JavaScript libraries such as jQuery.
"""

# Subsystems
# Subsystem 1: Order Processing
class OrderProcessing:
    def create_order(self, items):
        print(f"Creating order for items: {items}")
        return {"order_id": 123, "items": items}

    def confirm_order(self, order):
        print(f"Order {order['order_id']} confirmed.")
        return True


# Subsystem 2: Payment Processing
class PaymentProcessing:
    def process_payment(self, order, payment_details):
        print(f"Processing payment for order {order['order_id']} using {payment_details['method']}.")
        return {"payment_id": 987, "status": "Success"}

    def refund_payment(self, payment):
        print(f"Refunding payment {payment['payment_id']}.")
        return {"status": "Refunded"}


# Subsystem 3: Shipping
class Shipping:
    def arrange_shipping(self, order):
        print(f"Arranging shipping for order {order['order_id']}.")
        return {"tracking_number": "AMZ12345"}

    def track_package(self, tracking_number):
        print(f"Tracking package with tracking number: {tracking_number}")
        return {"status": "In Transit"}


# The Facade
class AmazonFacade:
    def __init__(self):
        self.order_processing = OrderProcessing()
        self.payment_processing = PaymentProcessing()
        self.shipping = Shipping()

    def place_order(self, items, payment_details):
        # Step 1: Create and confirm the order
        order = self.order_processing.create_order(items)
        if not self.order_processing.confirm_order(order):
            return {"status": "Order Failed"}

        # Step 2: Process the payment
        payment = self.payment_processing.process_payment(order, payment_details)
        if payment["status"] != "Success":
            return {"status": "Payment Failed"}

        # Step 3: Arrange for shipping
        shipping = self.shipping.arrange_shipping(order)

        return {
            "status": "Order Successful",
            "order": order,
            "payment": payment,
            "shipping": shipping,
        }

    def track_order(self, tracking_number):
        return self.shipping.track_package(tracking_number)


# Client code
def main():
    amazon = AmazonFacade()
    items = ["Book: Clean Code", "Laptop: MacBook Pro"]
    payment_details = {"method": "Credit Card", "card_number": "1234-5678-9876-5432"}

    # Placing an order
    order_result = amazon.place_order(items, payment_details)
    print("\nOrder Result:", order_result)

    # Tracking an order
    tracking_result = amazon.track_order(order_result["shipping"]["tracking_number"])
    print("\nTracking Result:", tracking_result)


if __name__ == "__main__":
    main()
