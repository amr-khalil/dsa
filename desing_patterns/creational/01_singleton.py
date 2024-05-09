"""
What is the singleton pattern?
The singleton pattern is a type of creational pattern that restricts the instantiation of a class to a single object.
This allows the class to create an instance of the class the first time it is instantiated. However, on the next try, the existing instance of the class is returned. No new instance is created.

Example
A real-life example is a printer a couple of office employees want to use. It’ll be a shared resource amongst all the employees.
Hence, a single instance of the printer is required so that everyone can share instead of having a new instance for each employee who wants to print something.

When to use the singleton pattern?
The singleton pattern is mostly used in cases where you want a single object to coordinate actions across a system. Singletons are mostly used by:
Services: services can be singleton since they store the state, configuration, and provide access to resources. Therefore, it makes sense to have a single instance of a service in an application.
Databases: when it comes to database connections, databases such as MongoDB utilize the singleton pattern.
Configurations: if there is an object with a specific configuration,you don’t need a new instance every time that configuration object is needed.

"""


class AmazonServiceConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AmazonServiceConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self, access_key, secret_key):
        if not hasattr(self, 'initialized'):
            self.access_key = access_key
            self.secret_key = secret_key
            self.initialized = True
            self.connection = self.connect_to_service()
            print("Amazon Service Connection Initialized!")

    def connect_to_service(self):
        # Simulate service connection initialization
        return f"Connected to Amazon service with Access Key: {self.access_key}"

    def get_connection(self):
        return self.connection

    def do_something(self):
        # Simulate doing some action on the service
        print("Performing an action on the Amazon service.")

# Usage
if __name__ == '__main__':
    # Initialize the Singleton instance
    connection1 = AmazonServiceConnection('access_key_123', 'secret_key_abc')
    print(connection1.get_connection())
    connection1.do_something()

    # Attempt to initialize a second instance with different credentials
    connection2 = AmazonServiceConnection('another_key_456', 'another_secret_key_def')
    print(connection2.get_connection())
    connection2.do_something()

    # Verify that both instances are the same
    print(f"connection1 is connection2: {connection1 is connection2}")
