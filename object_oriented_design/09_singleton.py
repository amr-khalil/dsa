class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class DatabaseManager(metaclass=Singleton):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        print(f"Connecting to database with {self.connection_string}")


class Logger(metaclass=Singleton):
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        print(f"Logging {message} to {self.log_file}")



class Singleton2(type):
    __instances = None

    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls.__instances


class DatabaseManager2(metaclass=Singleton2):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        print(f"Connecting to database with {self.connection_string}")


class Logger2(metaclass=Singleton2):
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        print(f"Logging {message} to {self.log_file}")




if __name__ == "__main__":
    db1 = DatabaseManager("sqlite://localhost/db1")
    db2 = DatabaseManager("mysql://localhost/db2")

    logger1 = Logger("app.log")
    logger2 = Logger("error.log")

    db1.connect()  # Connecting to database with sqlite://localhost/db1
    db2.connect()  # No connection, already connected to db1

    logger1.log("Info message")  # Logs "Info message" to app.log
    logger2.log("Error message")  # No log, already logging to app.log
    
    
    db1 = DatabaseManager2("sqlite://localhost/db1")
    db2 = DatabaseManager2("mysql://localhost/db2")

    logger1 = Logger2("app.log")
    logger2 = Logger2("error.log")

    db1.connect()  # Connecting to database with sqlite://localhost/db1
    db2.connect()  # No connection, already connected to db1

    logger1.log("Info message")  # Logs "Info message" to app.log
    logger2.log("Error message")  # Logs "Error message" to error.log
