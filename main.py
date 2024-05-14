from user_add import add_user
from user_fetch import view_user, view_all_users
from book_add import add_book
from book_fetch import view_book, view_all_books
from borrow_rent_book import borrow_book, return_book


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
            borrow_book(conn, user_id, book_id, borrow_date)
        elif action == "3":
            return_book(conn, user_id, book_id, return_date)
        elif action == "4":
            view_book()
        elif action == "5":
            view_all_books()
        elif action == "6":
            break
        else:
            print("Invalid Input, try again!")


while True:
    action = input(
        """
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
