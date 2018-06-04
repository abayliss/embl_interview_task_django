# EMBL Interview Task - Andrew Bayliss

This application implements the REST API for CRUD operations on Person objects set as part of my interview. The application is written in Python 3 and uses the Django framework and the Django REST Framework, along with an SQLite database.

## Running

First create a Python virtual environment:

```
python -m venv embl
```

Then activate it:

```
embl\Scripts\activate.bat # for Windows Command Prompt

source embl/bin/activate # for bash/zsh
```

Now install the required Python libraries:

```
pip install -r requirements.txt
```

Next, set up the database:

```
python manage.py migrate
```

Authentication is required to the the API, so now add a user to the database, any permissions will do:

```
python manage.py createsuperuser --email you@domain.com --username admin
```

Finally, run the application using the development server:

```
python manage.py runserver
```

You should see output like:

```
Performing system checks...

System check identified no issues (0 silenced).
June 02, 2018 - 14:10:50
Django version 2.0.5, using settings 'embl_interview_task_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

The application will now be available at the address shown in the output.

## Interacting with the API

You can use the cURL CLI tool to interact with the API like so:

```
curl -X POST http://user:password@localhost:8000/person/ -H 'Content-Type: application/json' -d '{"first_name": "Turanga", "last_name": "Leela", "age": 25, "favourite_colour": "purple" }'

curl -X GET http://user:password@localhost:8000/person/1/
```

You can also interact with the API using the web interface provided by the Django REST Framework by going to http://localhost:8000/person/ in a browser.

## Tests

Run the included tests like so:

```
python manage.py test 
```

The tests cover the model, and also the main operations of the API.

## Limitations

The database schema ideally would have indexes on at least the name fields.

Currently, any authenticated user can fully interact with the API. For a real world applicaton some privilege model should be implemented to allow different users to have different permissions on the API. For example, users could be allowed only read-only access.

I have not explored the security implications of the web interface provided by Django REST Framework, it could be that this should be disabled in a production environment.

I have only included settings suitable for running a development version of the application, no production configuration is provided.