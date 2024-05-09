"""
What is the flyweight pattern?

The Flyweight Design Pattern is useful when you have many objects that are similar and you want to minimize memory usage by sharing common state across those objects.

It is a structural pattern that focuses on how related objects share data.
It helps prevent repetitive code and increases efficiency when it comes to data sharing as well as conserving memory.
This pattern takes the common data structures/objects that are used by a lot of objects and stores them in an external object (flyweight) for sharing.
You could say that it is used for caching purposes. So, the same data does not need to have separate copies for each object, instead, it is shared amongst all.
A flyweight is an independent object that can be used in multiple contexts simultaneously. It cannot be distinguished from the instances of objects that are not sharable. A flyweight object can consist of two states:
intrinsic: this state is stored in the flyweight. It contains the information required by the internal methods of objects. It is independent of the context of the flyweight and is sharable with other objects.
extrinsic: this state depends on the context of the flyweight and it cannot be shared.
Normally, the client objects pass the extrinsic state to the flyweight object when needed.

When to use the flyweight pattern?
This pattern should be used when your application has plenty of objects using similar data or when memory storage cost is high.
JavaScript uses this pattern to share a list of immutable strings across the application.

This pattern is mostly used in applications like network apps or word processors. It can also be used in web browsers to prevent loading the same images twice. The flyweight pattern allows caching of images. Therefore, when a web page loads, only the new images are loaded from the Internet, the already existing ones are fetched from the cache.


"""


from typing import Dict

class ProductFlyweight:
    """
    The Flyweight stores shared state (intrinsic state).
    """
    def __init__(self, category: str, brand: str, image_url: str):
        self.category = category
        self.brand = brand
        self.image_url = image_url

    def display(self, item_code: str, price: float):
        """
        Displays the product with both intrinsic and extrinsic states.
        Intrinsic state: shared properties (category, brand, image_url)
        Extrinsic state: unique to each item (item_code, price)
        """
        print(f"Displaying {self.category} - {self.brand} (Item: {item_code}, Price: ${price:.2f})")
        print(f"Image URL: {self.image_url}")

class ProductFlyweightFactory:
    """
    Flyweight Factory to manage flyweight objects.
    """
    def __init__(self):
        self._flyweights: Dict[str, ProductFlyweight] = {}

    def _get_key(self, category: str, brand: str, image_url: str) -> str:
        return f"{category}-{brand}-{image_url}"

    def get_flyweight(self, category: str, brand: str, image_url: str) -> ProductFlyweight:
        key = self._get_key(category, brand, image_url)
        if key not in self._flyweights:
            print(f"Creating new flyweight for {key}")
            self._flyweights[key] = ProductFlyweight(category, brand, image_url)
        else:
            print(f"Reusing existing flyweight for {key}")
        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        for key in self._flyweights:
            print(f"\t{key}")

class ProductItem:
    """
    ProductItem represents the product with a unique extrinsic state.
    """
    def __init__(self, item_code: str, price: float, flyweight: ProductFlyweight):
        self.item_code = item_code
        self.price = price
        self.flyweight = flyweight

    def display(self):
        self.flyweight.display(self.item_code, self.price)

# Client Code
if __name__ == "__main__":
    # Flyweight factory
    factory = ProductFlyweightFactory()

    # Creating product items
    items = [
        ProductItem("A001", 29.99, factory.get_flyweight("Electronics", "Sony", "http://example.com/sony1.jpg")),
        ProductItem("A002", 19.99, factory.get_flyweight("Electronics", "Sony", "http://example.com/sony1.jpg")),
        ProductItem("B003", 49.99, factory.get_flyweight("Books", "Penguin", "http://example.com/penguin1.jpg")),
        ProductItem("B004", 39.99, factory.get_flyweight("Books", "Penguin", "http://example.com/penguin1.jpg")),
        ProductItem("E005", 499.99, factory.get_flyweight("Electronics", "Apple", "http://example.com/apple1.jpg")),
        ProductItem("E006", 599.99, factory.get_flyweight("Electronics", "Apple", "http://example.com/apple1.jpg")),
    ]

    # Display all product items
    for item in items:
        item.display()

    # List all flyweights in the factory
    factory.list_flyweights()
