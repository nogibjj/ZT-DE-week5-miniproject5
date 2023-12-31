import sqlite3

def connect_to_db(db_name):
    """
    Connects to a SQLite database and returns the connection and cursor.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor


def create_table(cursor):
    """
    Creates a table named 'users' if it does not exist.
    """
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
    ''')


def insert_data(cursor, name, age):
    """
    Inserts user data into the 'users' table.
    """
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))


def read_data(cursor):
    """
    Reads all data from the 'users' table.
    """
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()


def update_data(cursor, user_id, new_name):
    """
    Updates the name of a user given their user ID.
    """
    cursor.execute('UPDATE users SET name = ? WHERE id = ?', (new_name, user_id))


def delete_data(cursor, user_id):
    """
    Deletes a user given their user ID.
    """
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

if __name__ == "__main__":
    conn, cursor = connect_to_db("sample.db")
    create_table(cursor)


       # CRUD operations
    insert_data(cursor, "John Doe", 25)
    insert_data(cursor, "Jane Smith", 30)
    
    print("Data after insertions:")
    print(read_data(cursor))
    
    update_data(cursor, 1, "Johnathan Doe")
    
    print("Data after updating John Doe's name:")
    print(read_data(cursor))
    
    delete_data(cursor, 2)
    
    print("Data after deleting Jane Smith:")
    print(read_data(cursor))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


