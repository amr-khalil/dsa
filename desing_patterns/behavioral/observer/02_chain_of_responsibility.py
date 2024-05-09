"""
The Chain of Responsibility pattern is a behavioral design pattern used to pass a request along a chain of handlers. Each handler can either handle the request or pass it to the next handler in the chain.

The chain of responsibility pattern allows a request sent by a client to be received by more than one object. It creates a chain of loosely-coupled objects that, upon receiving the request, either handle it or pass it to the next handler object.

When to use the chain of responsibility pattern?
You can use it if your program is written to handle various requests in different ways without knowing the sequence and type of requests beforehand.
It allows you to chain several handlers, thus, allowing all of them a chance to process the request.

A good example of the use of the chain of responsibility pattern is in the process of event bubbling in the DOM,
where the event propagates through the nested elements,one of which may choose to handle the event.

Here's a Python example of implementing the Chain of Responsibility pattern using a simple e-commerce scenario inspired by Amazon.
In this example, we simulate an order request passing through various handlers (steps) like
payment processing => inventory checking => shipping preparation => and customer notification.
"""


from abc import ABC, abstractmethod


class OrderHandler(ABC):
    """
    Abstract Handler class for processing orders.
    """

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        """
        Process the request or forward it to the next handler.
        """
        if self._next_handler:
            return self._next_handler.handle(request)
        else:
            return request


class PaymentProcessingHandler(OrderHandler):
    """
    Handles payment processing.
    """

    def handle(self, request):
        if request.get("payment_successful", False):
            print("Payment successful.")
            return super().handle(request)
        else:
            print("Payment failed.")
            return "Order cannot be processed: Payment failed."


class InventoryCheckHandler(OrderHandler):
    """
    Handles inventory checking.
    """

    def handle(self, request):
        if request.get("items_in_stock", False):
            print("Items in stock.")
            return super().handle(request)
        else:
            print("Items out of stock.")
            return "Order cannot be processed: Items out of stock."


class ShippingPreparationHandler(OrderHandler):
    """
    Handles shipping preparation.
    """

    def handle(self, request):
        if request.get("address_valid", False):
            print("Address validated for shipping.")
            return super().handle(request)
        else:
            print("Invalid shipping address.")
            return "Order cannot be processed: Invalid shipping address."


class CustomerNotificationHandler(OrderHandler):
    """
    Handles customer notification.
    """

    def handle(self, request):
        print("Customer notified about the successful order.")
        return "Order processed successfully."


if __name__ == "__main__":
    # Creating the chain of responsibility
    payment = PaymentProcessingHandler()
    inventory = InventoryCheckHandler()
    shipping = ShippingPreparationHandler()
    notification = CustomerNotificationHandler()

    # Setting up the chain
    payment.set_next(inventory).set_next(shipping).set_next(notification)

    # Example order request
    order_request = {
        "payment_successful": True,
        "items_in_stock": True,
        "address_valid": True
    }

    result = payment.handle(order_request)
    print("\nResult:", result)

    # Example failed payment request
    order_request_failed_payment = {
        "payment_successful": False,
        "items_in_stock": True,
        "address_valid": True
    }

    result = payment.handle(order_request_failed_payment)
    print("\nResult:", result)

    # Example out-of-stock request
    order_request_out_of_stock = {
        "payment_successful": True,
        "items_in_stock": False,
        "address_valid": True
    }

    result = payment.handle(order_request_out_of_stock)
    print("\nResult:", result)
