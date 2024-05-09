class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Woof!"
    
    
class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Miau!"
    
    
def get_pet(pet="dog"):
    """The factory method"""
    factories = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return factories[pet]
    
# Prblem:
  
# d = Dog('test')
# c = Cat('test')

pet = get_pet('cat')
print(pet.speak())

