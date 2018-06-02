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

## Tests

Run the included tests like so:

```
python manage.py test 
```

The tests cover ...