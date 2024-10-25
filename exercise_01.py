class Book:
    def __init__(self, title, author, isbn=None): # initialize the book with title, author, and isbn number
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):  # initialize the library with an empty list of books
        self.books = []

    def add_book(self, book):
        self.books.append(book) # add book to the library

        with open('books.txt', 'a') as file:
            file.write(f'{book.title}, {book.author}, {book.isbn}\n') # store each book in books.txt while adding it to the library

    def find_books(self, title=None, author=None): # find books by title or author
        found_books = []
        for book in self.books:
            if (title and book.title == title) or (author and book.author == author):
                found_books.append(book)
        return found_books

    def remove_book(self, title=None, author=None): # remove books by title or author
        for book in self.books:
            if (title and book.title == title) or (author and book.author == author):
                self.books.remove(book)
                return book
            
book1 = Book("The Load Of The Rings", "J.R.R. Tolkien", "9780544003415")
book2 = Book("Rich Dad Poor Dad", "Robert T. Kiyosaki", "9781612680194")
library = Library()

# add book to the library
library.add_book(book1)
library.add_book(book2)

# find the book by title and author
book_find = library.find_books(title="The Load Of The Rings")
print(book_find[0].title)

book_find = library.find_books(author="Robert T. Kiyosaki")
print(book_find[0].title)

# remove the book by title
book = library.remove_book(title="The Load Of The Rings")
print(book.title + " has been removed")

book = library.remove_book(author="Robert T. Kiyosaki")
print(book.title + " has been removed")

