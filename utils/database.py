""" In memory database, a list """

books = []

def add_book(title, author):
    books.append({"title": title, "author": author, "read": False})