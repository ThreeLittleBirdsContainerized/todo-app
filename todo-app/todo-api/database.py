from flask_mysqldb import MySQL
import random
import os


class Database:
    """
    Database class to handle database connection and queries
    """
    def __init__(self, app, table="tasks"):
        # Enter your database connection details below
        app.config['MYSQL_HOST'] = os.environ["DB_SERVICE_SERVICE_HOST"]
        app.config['MYSQL_PORT'] = int(os.environ["DB_SERVICE_SERVICE_PORT"])
        app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
        app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
        app.config['MYSQL_DB'] = os.environ["MYSQL_DATABASE"]

        # Intialize MySQL
        self.mysql = MySQL(app)
        self.prefix="MySQL:"
        self.table=table

        # Check if table exists using MySQL
        with app.app_context():
            cursor = self.mysql.connection.cursor()
            cursor.execute(f"SHOW TABLES LIKE '{self.table}'")
            result = cursor.fetchone()
            if result:
                print(f"{self.prefix} Table '{self.table}' found.")
            else:
                cursor.execute(
                    f"CREATE TABLE {self.table} (uid INT AUTO_INCREMENT PRIMARY KEY, id INT, title VARCHAR(255), description VARCHAR(255))"
                )
                # Saving the Actions performed on the DB
                self.mysql.connection.commit()
                print(f"{self.prefix} Table '{self.table}' created.")

            cursor.close()

    def generateId(self):
        """
        Generates a random id of 8 digits for a new record
        :return: Integer representing the id
        """
        id = ""
        while True:
            for i in range(8):
                id += str(random.randint(0, 9))

            if self.check(id):
                id = ""
            else:
                break
        return int(id)

    def check(self, id: int):
        # Check if id exists using MySQL
        cursor = self.mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE id = '{id}'")
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return False
        else:
            return True

    def register(self, task: str, description: str):
        id = self.generateId()

        # Insert new record using MySQL
        cursor = self.mysql.connection.cursor()
        print(f"INSERT INTO {self.table} (id, title, description) VALUES ({id}, {task}, {description})")
        cursor.execute(f"INSERT INTO {self.table} (id, title, description) VALUES ({id}, %(title)s, %(description)s)", {"title": task, "description": description})
        # Saving the Actions performed on the DB
        self.mysql.connection.commit()
        print(f"{self.prefix} {id} Registered.")
        cursor.close()
        return id

    def delete(self, id: int):
        # Delete record using MySQL
        cursor = self.mysql.connection.cursor()
        cursor.execute(f"DELETE FROM {self.table} WHERE id = '{id}'")
        # Saving the Actions performed on the DB
        self.mysql.connection.commit()
        print(f"{self.prefix} {id} Deleted.")
        cursor.close()

    def updateTitle(self, id: int, value: str):
        # Update record using MySQL
        cursor = self.mysql.connection.cursor()
        cursor.execute(f"UPDATE tasks SET title = '{value}' WHERE id = {id}")
        # Saving the Actions performed on the DB
        self.mysql.connection.commit()
        print(f"{self.prefix} {id} Changed title in {id} to {value}.")
        cursor.close()

    def updateDescription(self, id: int, value: str):
        # Update record using MySQL
        cursor = self.mysql.connection.cursor()
        cursor.execute(f"UPDATE tasks SET description = '{value}' WHERE id = {id}")
        # Saving the Actions performed on the DB
        self.mysql.connection.commit()
        print(f"{self.prefix} {id} Changed description in {id} to {value}.")
        cursor.close()

    def getData(self, id: int):
        # Read a record using MySQL
        cursor = self.mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE id = '{id}'")
        result = cursor.fetchone()
        cursor.close()
        return result

    def list(self):
        # Read records using MySQL
        cursor = self.mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        result = cursor.fetchall()
        cursor.close()
        return [{"id": line[1], "title": line[2], "description": line[3]} for line in result]

