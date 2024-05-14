from db_connection import connect_db, Error
from book_fetch import view_all_books

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("What is book's title? ").title()
            isbn = int(input("What is book's isbn? "))
            publication_date = input("What is book's publication date? ")

            new_book = (title, isbn, publication_date)

            query = "INSERT INTO Books (title, isbn, publication_date) VALUES (%s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit() 
            print(f"New Book {title} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()