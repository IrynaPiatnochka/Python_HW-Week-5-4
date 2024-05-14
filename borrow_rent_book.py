from db_connection import connect_db, Error

def borrow_book(conn, user_id, book_id, borrow_date):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        availability = cursor.fetchone()[0]
        if availability == 0:
            print("Book is not available.")
            return

        cursor.execute("""
            INSERT INTO borrowed_books (user_id, book_id, borrow_date)
            VALUES (%s, %s, %s)
        """, (user_id, book_id, borrow_date))

        cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))

        conn.commit()
        print("Book borrowed successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()

def return_book(conn, user_id, book_id, return_date):
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM borrowed_books
            WHERE user_id = %s AND book_id = %s
        """, (user_id, book_id))
        record = cursor.fetchone()
        if not record:
            print("User has not borrowed this book.")
            return

        cursor.execute("""
            UPDATE borrowed_books
            SET return_date = %s
            WHERE user_id = %s AND book_id = %s
        """, (return_date, user_id, book_id))

        cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))

        conn.commit()
        print("Book returned successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        borrow_book()
        return_book()
        conn.close()