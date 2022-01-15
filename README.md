# todo-list

### Database setup

- Install MySQL and run the server on the port 3306 (on Ubuntu `sudo apt-get install mysql-server` and `sudo mysql_secure_installation utility` to setupt the password for root)
- access to the db using `sudo mysql -u root -p`
- Create an user with 
  ```
  CREATE USER 'todo'@'localhost' IDENTIFIED BY 'P@s$w0rd123!';
  GRANT ALL PRIVILEGES ON * . * TO 'todo'@'localhost';
  FLUSH PRIVILEGES;
  \q
  ```
- Login with the new user `mysql -u todo -p`
- Create the database `CREATE DATABASE todo;`

### Run Flask
- In the folder path install the dependecies with `pip install -r requirements.txt'
- Run flask with `python main.py`

### View the website

- Connect to the http://127.0.0.1:5500/

![Homepage](./img/homepage.png)


### API structure
Each element below is exactly the name of the API. ERROR-DESCRIPTION means the error that the UI should show:
- new: (POST)
  - SENT (json)
    ```
    { "id": ..,
      "title": ..,
      "description": ..
    }
    ```
  - RETURN 
    - if success 
       ```
       "", 220
       ```
     - else failure
       ```
       { "Response": "ERROR-DESCRIPTION" }, 500
       ```
       
- edit: (POST)
  - SENT (json)
    ```
    { "id": ..,
      "title": ..,
      "description": ..
    }
    ```
  - RETURN 
    - if success 
     ```
     "", 220
     ```
    - else failure
     ```
     { "Response": "ERROR-DESCRIPTION"}, 500
     ```
  
- delete: (GET)
  - SENT (int)
     ```id```
  - RETURN 
    - if success 
       ```
       "", 220
       ```
     - else failure
       ```
       { "Response": "ERROR-DESCRIPTION" }, 500
       ```
       
- tasks: (GET)
  - SENT
    ```
    nothing
    ```
  - RETURN 
    - if success (list of json object)
       ```
       [{ "id": ..,
        "title": ..,
        "description": ..
        },
        { "id": ..,
          "title": ..,
          "description": ..
        }]
        , 200
        ```
    - else failure
       ```
       { "Response": "ERROR-DESCRIPTION" }, 50
       ```
       
       
 ### WORK DIVISION
- Behnam:
  - [ ] Add Angular to the project
  - [ ] Refactor UI
- Simmy:
  - [ ] Refactor API following what is written in API structure section
- Peppe:
  - [ ] Automatize (Dockerfile (?)) the creation of the database
