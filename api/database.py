import mysql.connector
import random
import os

from werkzeug.utils import validate_arguments

prefix = "MySQL:"

mydb = mysql.connector.connect(
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"],
)

cursor = mydb.cursor()


def init():
    sql = "SHOW TABLES LIKE 'tasks'"
    cursor.execute(sql)
    res = cursor.fetchone()
    if res:
        print(f"{prefix} Table 'tasks' found.")
        return
    else:
        cursor.execute(
            "CREATE TABLE tasks (uid INT AUTO_INCREMENT PRIMARY KEY, id INT, title VARCHAR(255), description VARCHAR(255))"
        )
        print(f"{prefix} Table 'tasks' created.")
        return


def generateId():
    id = ""
    while True:
        for i in range(8):
            id += str(random.randint(0, 9))

        if check(id):
            id = ""
        else:
            break

    return int(id)


def register(task: str, description: str):
    sql = "INSERT INTO tasks (id, title, description) VALUES (%s, %s, %s)"
    id = generateId()
    val = (id, task, description)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"{prefix} {id} Registered.")
    return id


def delete(id: int):
    sql = f"DELETE FROM tasks WHERE id = '{id}'"
    cursor.execute(sql)
    mydb.commit()
    print(f"{prefix} {id} Deleted.")


def updateTitle(id: int, value: str):
    sql = f"UPDATE tasks SET title = %s WHERE id = %s"
    val = (value, id)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"{prefix} Changed title in {id} to {value}.")


def updateDescription(id: int, value: str):
    sql = f"UPDATE tasks SET description = %s WHERE id = %s"
    val = (value, id)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"{prefix} Changed description in {id} to {value}.")


def getData(id: int):
    cursor = mydb.cursor(buffered=True)
    cursor.execute(f"SELECT * FROM tasks WHERE id = '{id}'")
    res = cursor.fetchone()
    return res


def list():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM tasks")
    res = cursor.fetchall()
    return [{"id": line[1], "title": line[2], "description": line[3]} for line in res]


def check(id: int):
    cursor = mydb.cursor(buffered=True)
    cursor.execute(f"SELECT * FROM tasks WHERE id = '{id}'")
    res = cursor.fetchone()

    if res is None:
        return False
    else:
        return True
