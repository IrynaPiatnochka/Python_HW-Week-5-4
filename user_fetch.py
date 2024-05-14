from db_connection import connect_db, Error

def view_all_users():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Users;"

            cursor.execute(query)

            for row in cursor.fetchall():
                print(f"{row[0]}.) {row[1]}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() 
            conn.close()


def view_user():
    conn = connect_db()
    if conn is not None:
        try:
            user_id = int(input("What is the id of the user you're lookin for? "))
            cursor = conn.cursor()

            query = 'SELECT * FROM Users WHERE id = %s'

            cursor.execute(query, (user_id,))

            row = cursor.fetchall()[0]
            print(f"{row[0]}.) {row[1]}'s Contact info Email: {row[2]}.")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()