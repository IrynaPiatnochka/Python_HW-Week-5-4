from user_add import add_user
from user_fetch import view_user, view_all_users
from book_add import add_book
from book_fetch import view_book, view_all_books
from borrow_rent_book import borrow_book, return_book
from datetime import datetime


def user_menu():

    while True:
        action = input(
            """
    1.) Add User
    2.) View User Details
    3.) Display All Users
    4.) Main Menu
    > """
        )

        if action == "1":
            add_user()
        elif action == "2":
            view_user()
        elif action == "3":
            view_all_users()
        elif action == "4":
            break
        else:
            print("Invalid Input, please try again!")


def book_menu():

    while True:
        action = input(
            """
    1.) Add a new book 
    2.) Borrow a book
    3.) Return a book
    4.) Search for a book
    5.) Display all books
    6.) Main Menu
    > """
        )

        if action == "1":
            add_book()
        elif action == "2":
            user_id = input('What is your ID? ')
            book_title = input('What is the book title you want to borrow? ')
            borrow_date = datetime.strptime(input('What is the borrow date(format YYYY-MM-DD: '), '%Y-%m-%d')
            borrow_book(user_id, book_title, borrow_date) 
        elif action == "3":
            user_id = input('What is your ID? ')
            book_title = input('What is the book title you want to return? ')
            return_date = datetime.strptime(input('What is the return date(format YYYY-MM-DD: '), '%Y-%m-%d')
            return_book(user_id, book_title, return_date) 
        elif action == "4":
            title = input('What is the title of the book? ')
            view_book(title)
        elif action == "5":
            view_all_books()
        elif action == "6":
            break
        else:
            print("Invalid Input, try again!")


while True:
    action = input(
        """2
    
    1.) User Actions
    2.) Book Actions
    3.) Quit
    > """
    )

    if action == "1":
        user_menu()
    elif action == "2":
        book_menu()
    elif action == "3":
        break
    else:
        "Invalid Response, please try again"
