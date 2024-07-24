import sqlite3
from sqlite3 import Error


class SQLSetup:
    def __init__(self, db_file):
        """Initialize the SQLiteDB object with the database file."""
        self.db_file = db_file
        self.connection = None

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Connection to {self.db_file} established.")
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print(f"Connection to {self.db_file} closed.")

    def execute_query(self, query, params=None):
        """Execute a query on the SQLite database."""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error: {e}")

    def execute_read_query(self, query, params=None):
        """Execute a read query on the SQLite database and return the results."""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error: {e}")
            return None

    def create_table(self, create_table_sql):
        """Create a table with the provided SQL statement."""
        self.execute_query(create_table_sql)
