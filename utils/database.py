from .database_connection import DatabaseConnection
# change git branch to watch the normal version without context manager

# Create initial database
def create_book_table():
    # Create a connection with the database, while creating it if it is the first time and it does not exist yet
    with DatabaseConnection() as connection:
        # Create cursor out of this database to handle it
        cursor = connection.cursor()
    
        # Create table (query) inside this database: the SQL query goes between the quotation as a string
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY, author TEXT, status INTEGER)')
    
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
    connection.close()
    

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


def mark_book_read(title):
    
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('UPDATE books SET status = 1 WHERE name = ?', (title,))
    
    connection.commit()
    connection.close()

def delete_book(title):    
    
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('DELETE FROM books WHERE name = ?', (title,))
    connection.commit()
    connection.close()