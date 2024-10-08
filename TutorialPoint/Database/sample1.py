import psycopg2
import time


# Function to check if a database already exists
def check_database_exists(db_name):
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='vishalSP*96',
            database='postgres',
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Check if the database exists (use lowercase)
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name.lower()}';")
        exists = cur.fetchone()

        cur.close()
        conn.close()

        return exists is not None

    except Exception as e:
        print(f"Error checking database existence: {e}")
        return False


# Function to create the database
def create_database():
    db_name = 'newdb'  # Use lowercase for database names
    try:
        if not check_database_exists(db_name):
            conn = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='vishalSP*96',
                database='postgres',
            )
            conn.autocommit = True  # Allow database creation without commit
            cur = conn.cursor()

            # Create the new database (in lowercase)
            cur.execute(f'CREATE DATABASE {db_name};')
            print(f"Database '{db_name}' created successfully!")

            cur.close()
            conn.close()

            # Add a delay to ensure the database is ready
            time.sleep(2)
        else:
            print(f"Database '{db_name}' already exists!")

    except Exception as e:
        print(f"Error creating database: {e}")


# Function to create a table in the new database
def create_table():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='newdb',  # Use lowercase database name
            user='postgres',
            password='vishalSP*96'
        )
        cur = conn.cursor()

        # Create the table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INTEGER,
                department VARCHAR(50)
            )
        ''')
        print("Table 'employees' created successfully!")

        conn.commit()  # Commit the transaction after creating the table
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error creating table: {e}")


# Function to insert data into the table
def insert_data():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='newdb',  # Use lowercase database name
            user='postgres',
            password='vishalSP*96'
        )
        cur = conn.cursor()

        # Insert data into the table
        cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ('Alice', 30, 'HR'))
        cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ('Bob', 45, 'Engineering'))
        conn.commit()  # Commit the transaction after inserting data

        print('Data inserted successfully!')

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error inserting data: {e}")


# Function to retrieve data from the table
def retrieve_data():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='newdb',  # Use lowercase database name
            user='postgres',
            password='vishalSP*96'
        )
        cur = conn.cursor()

        # Retrieve data from the table
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()

        # Display the data
        print("Data from 'employees' table:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error retrieving data: {e}")


# Run the steps in sequence
create_database()  # Create the database
create_table()  # Create the table in the new database
insert_data()  # Insert data into the table
retrieve_data()  # Retrieve and display the data
