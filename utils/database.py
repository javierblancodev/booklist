""" In memory database, a list """

books = []

def display_books():
    
    if len(books) > 0:
        
        for book in books:
            if book["read"]:
                status = "Finished"
            else:
                status = "Unfinished"
            print(f'Book title: {book["title"]}, author: {book["author"]}, status: {status}')

    else:
        print('You have no books in your collection yet')

def add_book(title, author):
    books.append({"title": title, "author": author, "read": False})

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