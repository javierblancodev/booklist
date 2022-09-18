from multiprocessing import connection
import sqlite3

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
    # Create a connection with the database, while creating it if it is the first time and it does not exist yet
    connection = sqlite3.connect('data.db')
    # Create cursor out of this database to handle it
    cursor = connection.cursor()
    
    # Create table (query) inside this database: the SQL query goes between the quotation as a string
    cursor.execute('CREATE TABLE books(name TEXT PRIMARY KEY, author TEXT, status INTEGER)')
    # SQLIte only support 5 types of data that can be null , integer, real (float), text (strings), blob (binary datafile to store images, documents, pdf...)
    
    # Commit queries that are held in memory for this database
    cursor.commit()
    # Close connection

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