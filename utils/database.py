""" 
Format of the csv file: 
name,author,read\n 
"""

BOOKS_FILE = 'books.txt'

def add_book(title, author):
    with open(BOOKS_FILE, 'a') as file:
        file.write(f'{title},{author},False\n')

def get_all_books():
    with open(BOOKS_FILE, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2] } for line in lines
    ]


def mark_book_read(title):
    books = get_all_books()
    for book in books:
        if book["name"] == title:
            book["read"] = "True"
            break
    else:
        print(f'Sorry, {title} is not recorded among your books')
    _save_all_books(books)
    
    
def _save_all_books(books): 
    """ We use underscore at front to tell other developers not to use this function.
        It is like a private function in other programming languages but only conceptually, 
        since python does not have this feature"""

    with open(BOOKS_FILE, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")

def delete_book(title):    
    
    books = get_all_books()
    
    filtered_books = [ book for book in books if book['name'] != title ]
    
    if len(books) == len(filtered_books):
        print("Sorry, the book {} has not been registered yet".format(title))
    
    else: 
        _save_all_books(filtered_books)
        print("{} has been successfully deleted".format(title))