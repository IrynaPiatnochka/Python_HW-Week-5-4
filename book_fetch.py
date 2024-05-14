from db_connection import connect_db, Error


def view_all_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Books;"

            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()


def view_book(title):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Books WHERE title = %s;"

            cursor.execute(query, (title))

            print(cursor.fetchall())

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()


