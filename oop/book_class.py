# book_class.py

class Book:
    """
    Represents a book with a title, author, and publication year.
    Demonstrates Python magic methods: __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.") # Optional: for better visibility of creation

    def __del__(self):
        """
        Destructor method, called when the object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the informal string representation of the Book object,
        used by print() and str().
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the Book object,
        used by repr() and in interactive interpreters.
        The string should be an unambiguous representation that could be used
        to recreate the object.
        Format: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


# main.py (for testing the Book class)

def main():
    """
    Main function to demonstrate the Book class and its magic methods.
    """
    print("--- Demonstrating Book Class ---")

    # Creating an instance of Book
    # This will call __init__
    my_book = Book("1984", "George Orwell", 1949)
    print("\n")

    # Demonstrating the __str__ method
    # When print() is called on an object, it implicitly uses __str__
    print("Using print(my_book) [__str__]:")
    print(my_book)
    print("\n")

    # Demonstrating the __repr__ method
    # When repr() is explicitly called, it uses __repr__
    print("Using print(repr(my_book)) [__repr__]:")
    print(repr(my_book))
    print("\n")

    # Deleting a book instance to trigger __del__
    # The __del__ method will be called when the object's reference count drops to zero,
    # which happens here when 'del my_book' is executed.
    print("Deleting my_book to trigger __del__:")
    del my_book
    print("Book instance deleted (or marked for deletion by garbage collector).\n")

    # Note: Sometimes __del__ might not be called immediately due to Python's
    # garbage collection timing, especially in interactive environments or if
    # other references exist. In this simple script, it should be immediate.

if __name__ == "__main__":
    main()
