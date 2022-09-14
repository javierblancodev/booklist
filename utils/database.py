import json

""" 
Format of the json file: 

[
    {
        'name': 'Clean Code',
        'author': 'Robert,
        'read': True
    }
]

"""

BOOKS_FILE = 'books.json'

# Create initial database
def create_book_table():
    with open(BOOKS_FILE, 'w') as file:
        json.dump([], file)        


def add_book(title, author):
    books = get_all_books()
    books.append({'name': title, 'author': author, 'read': False})
    _save_all_books(books)
    

def get_all_books():
    with open(BOOKS_FILE, 'r') as file:
        return json.load(file)


def _save_all_books(books): 
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file)
            


def mark_book_read(title):
    books = get_all_books()
    for book in books:
        if book["name"] == title:
            book["read"] = True
            break
    else:
        print(f'Sorry, {title} is not recorded among your books')
    _save_all_books(books)


def delete_book(title):    
    
    books = get_all_books()
    filtered_books = [ book for book in books if book['name'] != title ]
    
    if len(books) == len(filtered_books):
        print("Sorry, the book {} has not been registered yet".format(title))
    else: 
        _save_all_books(filtered_books)
        print("{} has been successfully deleted".format(title))