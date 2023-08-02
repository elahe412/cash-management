# Cash Management System

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/elahe412/cash-management.git
$ cd cash-management
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

```sh
(env)$ cd project
(env)$ python manage.py migrate
In case of need sample data you can run this command, otherwise you could create data by the api or the admin panel
(env)$ python manage.py loaddata fixtures/category.json --app transaction.Category
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

## Docker

To deploy project with docker you should follow these steps:

```sh
$ cd sample-django-app
$ docker build . -t cash_management
$ docker run -p 8000:8000 cash_management:latest
```

And navigate to `http://127.0.0.1:8000/`.

## Docs

You can access API documentation with swagger available on `http://127.0.0.1:8000/doc/`.

## Walkthrough

In this application any user can register and login by email.
Each user can create,update and delete transactions with different kinds and categories;Also, users could be able to
filter and sort transactions based on different criteria (e.g., date, category)
The amount of users balance is available on their profile.
Users should be able to generate reports to analyze their cash flow in specific time or total expenses or incomes based
on categories.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:

```sh
(env)$ python manage.py test 
```