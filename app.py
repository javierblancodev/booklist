from click import prompt
from utils import database

print('Welcome to Booklyapp!')

run_program = True

USER_OPTIONS = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit\n
"""

def user_input(message):
    data = input(f'{message}\n').title()
    return data


def menu(run_program):
    
    while run_program:
        user_choice = input(USER_OPTIONS).lower()
        
        if user_choice == 'a':
            prompt_add_book()
        elif user_choice == 'l':
            list_books()
        elif user_choice == 'r':
            prompt_read_book()
        elif user_choice == 'd':
            prompt_delete_book()
        elif user_choice == 'q':
            run_program = False
        else:
            print('Sorry, I do not understand you. Please, try again.')


def prompt_add_book():
    title = user_input('Please introduce the title of the book you want to add')
    author = user_input('Please introduce the author\'s name')
    database.add_book(title, author)


def list_books():
    print("These are your books:")
    books = database.get_all_books()
    if len(books) > 0:
        
        for book in books:
            if book["read"]:
                status = "Finished"
            else:
                status = "Unfinished"
            print(f'Book title: {book["title"]}, author: {book["author"]}, status: {status}')
    else:
        print('You have no books in your collection yet')


def prompt_read_book():
    title = user_input('Please introduce the title of the book you want to mark as read')
    database.mark_book_read(title)


def prompt_delete_book():
    title = user_input('Please introduce the title of the want you want to delete')
    database.delete_book(title)


menu(run_program)

print("Come Back Soon!")