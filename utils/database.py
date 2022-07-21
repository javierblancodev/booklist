""" In memory database, a list """

books = []

def add_book(title, author):
    books.append({"title": title, "author": author, "read": False})

def mark_book_read(title):
    print(f'executed with title: {title}')
    print(f'inside function: {books}')
    for book in books:
        if book["title"] == title:
            book["read"] = True
            print(f'The book {book["title"]} has been successfully updated')