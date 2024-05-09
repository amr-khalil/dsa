"""
Encapsulation is the process of restricting access to methods and variables in a class in order to prevent direct modification of the data.
why: Encapsulation is important because it prevents external users from changing the internal state of an object at will, which can lead to unexpected or inconsistent behavior.
"""

class Movie:
    def __init__(self, title, year, genre):
        self.__title = title
        self.__year = year
        self.__genre = genre
    
    @property    
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def get_year(self):
        return self.__year

    def set_year(self, value):
        self.__year = value

    def get_genre(self):
        return self.__genre

    def set_genre(self, value):
        self.__genre = value

    def print_details(self):
        print("Title:", self.title)
        print("Year:", self.get_year())
        print("Genre:", self.get_genre())


def main():
    movie = Movie("The Lion King", 1994, "Adventure")
    movie.print_details()

    print("---")
    movie.title = "Forrest Gump"
    print("New title:", movie.title)
    

class Circle:
    def __init__(self, radius=0):
        self.__radius = radius
        
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, values):
        if values < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = values

if __name__ == '__main__':
    c = Circle()
    c.radius = 10
    print(c.radius)  # 5
    
