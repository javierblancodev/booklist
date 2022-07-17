from turtle import title
from utils import database

print('Welcome to Booklyapp!')

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice"""

def get_title(message):
    title = input(f'{message}\n')
    return title

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        
        if user_input == 'a':
            title = get_title('Please introduce the title of the book you want to add')
            # pass it to a function in the database to store the book there
        if user_input == 'l':
            pass
        if user_input == 'r':
            title = get_title('Please introduce the title of the book you want to mark as read')
            # pass it to a function in the database to mark the book as read there
        if user_input == 'd':
            title = get_title('Please introduce the title of the want you want to delete')
            # pass it to a function in the database to delete the book there

# def prompt_add_book ask for name and author
# def list_books shows all books in our list
# def prompt_read_book ask for a book name and change it to "read" in our list
# def prompt_delete_book ask for a book name and remove book from list

print(database.books)