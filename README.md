# todo-list

### Database setup

- Install MySQL and run the server on the port 3306 (on Ubuntu `sudo apt-get install mysql-server`)
- access to the db using `mysql -u root -p`
- Create an user with 
  ```CREATE USER 'todo'@'localhost' IDENTIFIED BY 'password';
  GRANT ALL PRIVILEGES ON * . * TO 'todo'@'localhost';
  FLUSH PRIVILEGES;
  \q```
- Login with the new user `mysql -u todo -p`
- Create the database `CREATE DATABASE todo;`

### Run Flask
- In the folder path install the dependecies with `pip install -r requirements.txt'
- Run flask with `python main.py`
