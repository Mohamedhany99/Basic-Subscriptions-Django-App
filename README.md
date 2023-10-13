## How to run the application

* clone the application

* create a virtual environment to contain the project (for example: virtualenv venv)

* activate the virtual environment for windows: (source venv/Scripts/activate) for linux: (source venv/bin/activate)

* create .env file and add the SECRET_KEY as a environment variable

* install the requirements (pip install -r requirements.txt)

* install MySQL database and configure it on your machine or inside the virtual environment
    after installing the MySQL server and run it successfuly add the DataBase configuration in the .env file as follows
    * NAME: It indicates the name of the database we want to connect.
    * USER: The MYSQL username is the one who has access to the database and manages it.
    * PASSWORD: It is the password of the database. 
    * HOST: It is indicated by “127.0.0.1”.
    * PORT: “3306” that the MySQL database is accessible at hostname “0.0.1” and on port “3306”


* create the database

    * python manage.py makemigrations
    * python manage.py migrate

* create the super user (Optional)

    * python manage.py createsuperuser
    * follow the instructions

* run the application
    * python manage.py runserver

## Dtabase Scheme Diagram
* you can view the database scheme diagram in the project called my_database_diagram.png
![database scheme diagram](my_database_diagram.png)

## Dockerization
you need to install docker engine, and be activated

* build the docker image

    * docker build -t subscription_service .

* run your docker image

    * docker run -p 8000:8000 subscription_service



## Notes for navigation

* you can find the home page when accessing: http://localhost:8000/

* you can find the admin dashboard: http://localhost:8000/admin/
