"""
Design a shopping cart system that allows users to add items to their cart, remove items from their cart, and checkout.
add discount and coupon code, tax, shipping, and total price


class Item:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount  # Discount in percentage

class ShoppingCart:
    def __init__(self, tax_rate=0):
        self.items = []
        self.coupon_discount = 0  # Coupon discount in percentage
        self.tax_rate = tax_rate  # Tax rate in percentage

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def remove_item(self, item):
        for i, (cart_item, quantity) in enumerate(self.items):
            if cart_item == item:
                del self.items[i]
                return

    def apply_coupon(self, coupon_discount):
        self.coupon_discount = coupon_discount

    def calculate_taxes(self, amount):
        return amount * (self.tax_rate / 100)

    def total_price(self):
        total = 0
        for item, quantity in self.items:
            item_price = item.price * (1 - item.discount / 100)  # Apply item discount
            total += item_price * quantity
        
        total -= total * self.coupon_discount / 100  # Apply coupon discount
        total += self.calculate_taxes(total)  # Apply taxes
        return total

    def checkout(self):
        total_price = self.total_price()
        self.items = []  # Clear the cart after checkout
        self.coupon_discount = 0  # Reset coupon discount after checkout
        return total_price

# Example usage:
item1 = Item("Shirt", 20, 10)  # Item "Shirt" with 10% discount
item2 = Item("Jeans", 30, 5)   # Item "Jeans" with 5% discount

cart = ShoppingCart(tax_rate=8)  # 8% tax rate
cart.add_item(item1, quantity=2)
cart.add_item(item2, quantity=1)

cart.apply_coupon(15)  # Apply a 15% coupon discount

total_price = cart.checkout()
print("Total price including taxes after checkout:", total_price)
"""

class Item:
    def __init__(self, id, name, price, discount=0):
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
        

class ShoppingCart:
    def __init__(self, tax_rate=0):
        self.items = {}
        self.tax_rate = tax_rate
        
    def add_item(self, item: Item, quantity: int=1) -> None:
        self.items[item.id] = (item, quantity)
        print(item.name)
    
    def remove_item(self, item: Item) -> None:
        for i, (item, quantity) in enumerate(self.items):
            if item == item:
                del self.items[i]
                return
            
    def apply_coupon(self, discount: int) -> None:
        self.discount = discount
            
if __name__ == '__main__':
    item1 = Item("Shirt", 20, 10)
    item2 = Item("Jeans", 30, 5)
    
    cart = ShoppingCart(tax_rate=10)
    cart.add_item(item1, quantity=2)
    cart.add_item(item2, quantity=1)
    
    # total_price = cart.checkout()
    # print("Total price including taxes after checkout:", total_price)
            