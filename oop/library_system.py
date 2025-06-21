# library_system.py

class Book:
    """
    Base class for all types of books.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    Additional attribute:
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes a new EBook instance.
        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Represents a physical print book, inheriting from Book.
    Additional attribute:
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a new PrintBook instance.
        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Represents a library that manages a collection of books using composition.
    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.
        Args:
            book (Book): An instance of Book or its derived classes.
        """
        if isinstance(book, Book):
            self.books.append(book)
            # Removed: print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        if not self.books:
            print("The library is currently empty.")
            return

        # Removed: print("\n--- Books in the Library ---")
        for book in self.books:
            print(book) # The __str__ method of each book object will be called
        # Removed: print("----------------------------")

