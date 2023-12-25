# Uni Connect

A platform for student vendors in universities to market and sell their products and services.

## Setup

- Create a virtual environment
```
$ python -m venv env
```

- Activate the virtual environment
```
$ source env/bin/activate
```

- Install requirements
```
$ pip install -r requirements.txt
```

- Run development server
```
$ cd uni_connect
$ python manage.py runserver
```

- If a new dependency is added, add it to the requirements.txt file
```
$ pip freeze > requirements.txt
```
