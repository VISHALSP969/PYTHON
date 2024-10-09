import sqlite3

# create a connection to a database (or create a )
connection = sqlite3.connect('my_database.db')

# create a cursor object to interact with the database
cursor = connection.cursor()

# create a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
''')

# insert a row into the user table
cursor.execute('''
    INSERT INTO users (name,age,email)
    VALUES ('John Doe',30,'john@example.com')
''')

# commit the changes to the database
connection.commit()

# select data from the table
cursor.execute('''
    SELECT* FROM users
''')
rows = cursor.fetchall()

for row in rows:
    print(row)

# update a record
cursor.execute('''
    UPDATE users
    SET age=31
    WHERE name='John Doe'
''')

connection.commit()

# select data from the table
cursor.execute('''
    SELECT* FROM users
''')
rows = cursor.fetchall()

for row in rows:
    print(row)

# delete a record
cursor.execute('''
    DELETE FROM users
    WHERE id=2
''')

connection.commit()

# select data from the table
cursor.execute('''
    SELECT* FROM users
''')
rows = cursor.fetchall()

for row in rows:
    print(row)

