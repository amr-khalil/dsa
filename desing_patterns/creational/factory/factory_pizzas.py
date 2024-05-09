class Pizza:
    """Product"""
    def __init__(self):
        self._price = None
    def get_price(self):
        return self._price

class MashroomPizza(Pizza):
    """Concrete Product A"""
    def __init__(self):
        self._price = 10
        
class CheesePizza(Pizza):
    """Concrete Product B"""
    def __init__(self):
        self._price = 8

def create_pizza(pizza_type):
    """The factory method"""
    factories = dict(mashroom=MashroomPizza(), cheese=CheesePizza())
    return factories[pizza_type]

if __name__ == '__main__':
    pizza = create_pizza('cheese')
    print(pizza.get_price())
    pizza = create_pizza('mashroom')
    print(pizza.get_price())