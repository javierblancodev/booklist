""" In memory database, a list """

books = [2,4]

def add_book(title, author):
    books.append({"title": title, "author": author, "read": False})