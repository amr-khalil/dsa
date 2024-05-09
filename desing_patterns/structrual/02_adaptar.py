"""
The adapter pattern allows classes that have different interfaces (properties/methods of an object) to work together.
It translates the interface for a class to make it compatible with another class.
This pattern is useful if an API is modified or new implementations are added to it.
In this case, if the other parts of a system are still using the old API,
the adapter pattern will translate the interface so that the two can work together.

When to use the adapter pattern?
The adapter pattern is used when we need old APIs to work with new refactored ones 
or when an object needs to cooperate with a class that has an incompatible interface.
It can also be used to reuse the existing functionality of classes.
"""

# Existing AmazonAPI class which we want to adapt
class AmazonAPI:
    def search_product(self, keyword):
        # Simulating search functionality
        return f"Search results for '{keyword}' on Amazon"

# New interface that our client code expects
class ProductSearch:
    def search(self, query):
        pass

# Adapter class to adapt AmazonAPI to ProductSearch interface
class AmazonAdapter(ProductSearch):
    def __init__(self, amazon_api):
        self.amazon_api = amazon_api

    def search(self, query):
        # Call the appropriate method of AmazonAPI and return the result
        return self.amazon_api.search_product(query)

# Client code
def main():
    # Creating an instance of AmazonAPI
    amazon_api = AmazonAPI()

    # Creating an instance of AmazonAdapter and passing AmazonAPI instance to it
    adapter = AmazonAdapter(amazon_api)

    # Using the adapter to search for a product
    result = adapter.search("laptop")
    print(result)

if __name__ == "__main__":
    main()