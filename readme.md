# Library App

This is a simple library application written in Python. It allows you to add books to a library and list all the books in the library.

## Classes

### `Book`

A class representing a book.

#### Attributes:
- `title` (str): The title of the book.
- `author` (str): The author of the book.

#### Methods:
- `__init__(self, title, author)`: Initializes a new book with a title and an author.

### `Library`

A class representing a library.

#### Attributes:
- `books` (list): A list of books in the library.

#### Methods:
- `__init__(self)`: Initializes a new library with an empty list of books.
- `add_book(self, book)`: Adds a book to the library.
- `list_books(self)`: Lists all books in the library with their titles and authors.

## Usage

```python
from library_app import Book, Library

# Initialize the library
library = Library()

# Add books to the library
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book(book1)
library.add_book(book2)

# List all books in the library
print("Listing all books in the library:")
library.list_books()

AUTHOR
MOHIT MATHUR
ROLL NO. G23AI2034
