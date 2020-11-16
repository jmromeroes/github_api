# GitHub API
This is a very simple project where I've tried exploring a clean architecture, domain driven design and CQRS in a simple project using Django Rest Framework.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/jmromeroes/github_api.git
$ cd github_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements/dev.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies you can migrate the sqlite database:
```sh
(env)$ DJANGO_SETTINGS_MODULE="github_api.settings.dev" python manage.py migrate
```

Once the database has been migrated you can start scraping data from GitHub:

Scrape user information by username
```sh
(env)$ DJANGO_SETTINGS_MODULE="github_api.settings.dev" python manage.py scrape_user_information <username>
```

Scrape public repositories
```sh
(env)$ DJANGO_SETTINGS_MODULE="github_api.settings.dev" python manage.py scrape_repositories
```

Scrape public repositories by username
```sh
(env)$ DJANGO_SETTINGS_MODULE="github_api.settings.dev" python manage.py scrape_repositories_by_username <username>
```

Now to consult the database you can create an admin user with the `createsuperuser` command

```sh
(env)$  DJANGO_SETTINGS_MODULE="github_api.settings.dev" python manage.py createsuperuser
```

Fill all required information and then run the project
```sh
(env)$  DJANGO_SETTINGS_MODULE="github_api.settings.dev" python manage.py createsuperuser
```

Navigate to `http://localhost:8000/admin` and join with the credentials you set

To query the information from the database there are 3 urls:

For user information:
GET http://localhost:8000/github/public/users/<username>/

For public repositories information:
GET http://localhost:8000/github/public/repositories/

For public repositories by username information:
GET http://localhost:8000/github/public/users/<username>/repositories
