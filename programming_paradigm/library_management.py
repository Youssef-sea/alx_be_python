class Book:
    """
    Represents a book in the library with a title, author, and availability status.
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
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out if it's currently available.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"'{self.title}' by {self.author} has been checked out.")
            return True
        else:
            print(f"'{self.title}' is already checked out.")
            return False

    def return_book(self):
        """
        Marks the book as available if it's currently checked out.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"'{self.title}' by {self.author} has been returned.")
            return True
        else:
            print(f"'{self.title}' is already available.")
            return False

    def is_available(self):
        """
        Checks if the book is currently available (not checked out).

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"

