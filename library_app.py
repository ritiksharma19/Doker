# library_app.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for index, book in enumerate(self.books, start=1):
            print(f"Book {index}: {book.title} by {book.author}")

if __name__ == "__main__":
    library = Library()

    # Adding some initial books
    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(book1)
    library.add_book(book2)

    # List all books in the library
    print("Listing all books in the library:")
    library.list_books()

