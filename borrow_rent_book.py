from db_connection import connect_db, Error


def borrow_book(user_id, book_title, borrow_date):
    conn = connect_db()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT availability FROM books WHERE title = %s LIMIT 0,1;", (book_title,)
        )
        availability = cursor.fetchone()[0]
        print(availability)
        if availability == 0:
            print("Book is not available.")
            return

        cursor.execute(
            "INSERT INTO borrowed_books (user_id, title, borrow_date) VALUES (%s, %s, %s)",
            (user_id, book_title, borrow_date),
        )

        cursor.execute(
            "UPDATE books SET availability = 0 WHERE title = %s", (book_title)
        )

        conn.commit()
        print("Book borrowed successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()


def return_book(user_id, book_title, return_date):
    conn = connect_db()
    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM borrowed_books WHERE user_id = %s AND title = %s",
            (user_id, book_title),
        )
        record = cursor.fetchone()
        if not record:
            print("User has not borrowed this book.")
            return

        cursor.execute(
            "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND title = %s",
            (return_date, user_id, book_title),
        )

        cursor.execute(
            "UPDATE books SET availability = 1 WHERE title = %s", (book_title)
        )

        conn.commit()
        print("Book returned successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()


if __name__ == "__main__":
    conn = connect_db()
