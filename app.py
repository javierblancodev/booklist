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

def display_books():
    for book in database.books:
        if book["read"]:
            status = "Finished"
        else:
            status = "Unfinished"
        print(f'Book title: {book["title"]}, author: {book["author"]}, status: {status}')

def menu(run_program):
    
    while run_program:
        user_choice = input(USER_OPTIONS).lower()
        
        if user_choice == 'a':
            title = user_input('Please introduce the title of the book you want to add')
            author = user_input('Please introduce the author\'s name')
            database.add_book(title, author)
        elif user_choice == 'l':
            print("These are your books:")
            display_books()
        elif user_choice == 'r':
            title = user_input('Please introduce the title of the book you want to mark as read')
            database.mark_book_read(title)
            print(f'outsite function: {database.books}')
        elif user_choice == 'd':
            title = user_input('Please introduce the title of the want you want to delete')
            database.delete_book(title)
        elif user_choice == 'q':
            run_program = False
        else:
            print('Sorry, I do not understand you. Try again.')

menu(run_program)

print("Come Back Soon!")