""" In memory database, a list """

books = []


def add_book(title, author):
    books.append({"title": title, "author": author, "read": False})


def get_all_books():
    return books


def mark_book_read(title):
    for book in books:
        if book["title"] == title:
            book["read"] = True
            break
    else:
        print(f'Sorry, {title} is not recorded among your books')


def delete_book(title):    
    global books
    prov_collection = []
    exist = False
    
    # books = [book for book in books if book["title"] != title]
    
    for book in books:
        if book["title"] != title:
            prov_collection.append(book)
        else: 
            exist = True
    if exist:
        print(f'The book {title} has been removed from your collection')
    else:
        print(f'Sorry, {title} is not recorded among your books')
    books = prov_collection