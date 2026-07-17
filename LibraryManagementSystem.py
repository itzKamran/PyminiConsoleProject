

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):

        print("\n------ Library Books ------")

        for book in self.books:
            print(book.title, "-", book.author, "- Available:", book.available)

    def issue_book(self, title):

        for book in self.books:

            if book.title == title:

                if book.available:

                    book.available = False

                    print("Book Issued Successfully")

                else:

                    print("Book Already Issued")

                return

        print("Book Not Found")

    def return_book(self, title):

        for book in self.books:

            if book.title == title:

                book.available = True

                print("Book Returned Successfully")

                return

        print("Book Not Found")
library = Library()

book1 = Book("Python", "Guido")

book2 = Book("Java", "James")

book3 = Book("C++", "Bjarne")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

student1 = Student("Kamran", 101)

library.show_books()

library.issue_book("Python")

library.show_books()

library.return_book("Python")

library.show_books()
