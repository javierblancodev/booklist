
import sqlite3

# Create initial database
def create_book_table():
    # Create a connection with the database, while creating it if it is the first time and it does not exist yet
    connection = sqlite3.connect('data.db')
    # Create cursor out of this database to handle it
    cursor = connection.cursor()
    
    # Create table (query) inside this database: the SQL query goes between the quotation as a string
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY, author TEXT, status INTEGER)')
    # SQLIte only support 5 types of data that can be null , integer, real (float), text (strings), blob (binary datafile to store images, documents, pdf...)
    
    # Commit queries that are held in memory for this database
    connection.commit()
    # Close connection
    connection.close()

def add_book(title, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    # cursor.execute(f'INSERT INTO books VALUES("{title}", "{author}", 0)')
    # Although the approach above will also work, this can be useb by hacker to perfomr a sql injection attack since any text will be pass in the database 
    # (for example DROP TABLE) through the the variables. It is good practice therefore to follow the approach below where we place a tuple as second argument
    # and then sql3 will insert this values in place of ?
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))
    # Commit the changes we make to our database
    connection.commit()
    connection
    

def get_all_books():
    # set up connection with database
    connection = sqlite3.connect('data.db')
    # create a handler/cursor out of the connection to work with
    cursor = connection.cursor()
    
    # Execute some sql queries throughout that handler/cursor
    cursor.execute('SELECT * FROM books') # Extract selected data and create a table with it
    # At this point, the cursor is waiting at the top of the table for any instruction to go down one row by one
    # We can specify how many rows we want to fetch in its way down
    fetched_books = cursor.fetchall() # fetch all books with all the columns since we select in the SQL query
    # fetchall return a list of tuples: [(name, author, status), (name, author, status), (name, author, status)]
    books = [ {'name': name, 'author': author, 'read': status} for name, author, status in fetched_books]
    
    # connection.commit() We do not need to commit anything here since we have not make any change in our database, just read from.
    connection.close()
    
    return books


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