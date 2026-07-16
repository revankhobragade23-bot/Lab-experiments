class book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id 
        self.title = title
        self.author = author
        self.available = true 

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id} - {self.title} by {self.author} ({status})"
    
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_book = []

    def __str__(self):
        return f"{self.patron_id} _ {self.name}"

class Library:
    def __init__(self):
        self.books = []
        self.patron = []

    def add_book(self, book):
        self.book.append(book)
        print(f"book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patron.append(patron)
        print(f"patron '{patron.name}' registered successfully.")

    def issue_book(self, book_id, patron_id):
        book = self.find_book(book_id)
        patron = self.find_patron(patron_id)

        if book and patron:
            if book.availabe:
                book.available = False
                patron.borrowed_books.apppend(book)
                print(f"'{book.title}' has been issued to {patron.name}.")
            else:
                print("Sorry! This book is already issued.")
        else:
            print("Book or patron not found.")

    def return_book(self, book_id, patron_id):
        book = self.find_book(book_id)
        patron = self.find_patron(patron_id)

        if book and patron:
            if book in patron.borrowed_book:
                patron.borrowed_books.remove(book)
                book.available = True
                print(f"'{book.title}' has been returned successfully.")
            else:
                print("Book or patron not found.")

    def find_book(self, patron_id):
        for patron in self.patron:
            if patron.patron_id == patron_id:
                return book
            return None               

    def find_patron(self, patron_id):
        for patron in self.patron:
            if patron.patron_id == patron_id:
                return patron
            return None 

    def display_books(self):
        print("\nlibrary books:")
        for book in self.books:
            print(book)

library = Library()

library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Roi"))

library.display_books()

library.issue_book(101, 1)
library.issue_book(102, 2)

library.display_books()

library.return_book(101, 1)

library.display_books()
