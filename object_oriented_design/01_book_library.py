from dataclasses import dataclass


class Book:
    def __init__(self, title, author, total_pages, content=None) -> None:
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0
        self.is_active = False
        self.content = content

class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, book: Book) -> None:
        if book.title in self.books.keys():
            raise ValueError(f'{book.title} already exists in the library')  
        self.books[book.title] = book
        print(f'{book.title} added to the library')
        
    def add_books(self, books:list[Book]) -> None:
        for book in books:
            self.add_book(book)
            
    def remove_book(self, book: Book) -> None:
        del self.books[book.title]
        print(f'{book.title} removed from the library')
        
    def get_book(self, title: str) -> Book:
        return self.books[title]
    
    def get_books(self) -> list:
        return [b for b in self.books.keys()]
    
    def get_books_by_author(self, author: str) -> list:
        return [b for b in self.books.keys() if self.books[b].author == author]
   

class Display:
    def __init__(self, library: Library, font_size: int = 12):
        self.library = library
        self.font_size = font_size
        
    def read_book(self, title: str, page: int) -> None:
        book = self.library.get_book(title)
        book.is_active = True
        book.content = f'Page {page} content'
        words_per_page = 500 * (12 / self.font_size)
        return " ".join(book.content.split()[:words_per_page])
    
    def display_books(self) -> None:
        for b in self.library.books.keys():
            print(f'{b} by {self.library.books[b].author}')
            
    def display_books_by_author(self, author: str) -> None:
        for b in self.library.get_books_by_author(author):
            print(f'{b} by {self.library.books[b].author}')
            
    def display_active_books(self) -> None:
        for b in self.library.active_books():
            print(f'{b} by {self.library.books[b].author}')
    
if __name__ == '__main__':
    books = [
        Book('Learn python the hard way', 'John doe', 200),
        Book('Harry Potter', 'Alex Travolta', 151),
        Book('The Alchemist', 'Paulo Coelho', 180),
        Book('The Da Vinci Code', 'Dan Brown', 300),
        Book('The Great Gatsby', 'John doe', 150),
        Book('The Catcher in the Rye', 'J.D. Salinger', 230),
        Book('The Hobbit', 'J.R.R. Tolkien', 250),
        
    ]
    library = Library()
    library.add_books(books)
    print('----')
        
    display = Display(library)
    display.display_books_by_author('John doe', font_size=12)

    
