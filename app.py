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
            status = "finished"
        else:
            status = "unfinished"
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
            # pass it to a function in the database to mark the book as read there
        elif user_choice == 'd':
            title = user_input('Please introduce the title of the want you want to delete')
            # pass it to a function in the database to delete the book there
        elif user_choice == 'q':
            run_program = False
        else:
            print('Sorry, I do not understand you. Try again.')

# def prompt_add_book ask for name and author
# def list_books shows all books in our list
# def prompt_read_book ask for a book name and change it to "read" in our list
# def prompt_delete_book ask for a book name and remove book from list

menu(run_program)

print(database.books)