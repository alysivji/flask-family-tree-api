# Family Tree API

*Practice project to create a Family Tree API using Flask, SQLAlchemy, Alembic, Marshmallow, and pytest.*

## Instructions

### Installation

(Assumes you have pipenv installed)

1. `git clone` repo
1. `pipenv install`
1. `make migrate-up`
1. `make up`

### Makefile Commands

```console
cat Makefile
up:
  pipenv run python manage.py

migration:
  pipenv run flask db migrate -m="$(m)"

migrate-up:
  pipenv run flask db upgrade

migrate-down:
  pipenv run flask db downgrade

shell:
  pipenv run ipython -i scripts/shell.py

test:
  pipenv run pytest

test-pdb:
  pipenv run pytest --pdb

test-cov:
  pipenv run pytest --cov

test-cov-view:
  pipenv run pytest --cov --cov-report html && open ./htmlcov/index.html
```

## API Endpoints

### `/api/v1/Person`

- *GET*
- *POST*

### `/api/v1/Person/{person_id}`

- *GET*
- *PUT*
- *DELETE*

### `/api/v1/Person/{person_id}/relationship`

- *POST*
- *DELETE*

## Todo

- [x] testing config
- [x] migrations
- [x] marshmallow
- [x] data model
- [x] CRUD endpoints for all tables
- [ ] relationship query endpoint
- [ ] swagger docs via apispec
- [ ] relationship details, start date, stop date
- [ ] logging
- [ ] spousal relationship
- [ ] marshmallow validation to make sure relations make sense (parent has earlier birthday than child)
- [ ] family table with information about year and place of origin, family crest image URL, greatest ancestors

## Resources

- [Flask Docs: App Factories](http://flask.pocoo.org/docs/1.0/patterns/appfactories/)
- [Flask Mega Tutorial: App Factories](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)
- [Genealogy Data Model](http://www.databaseanswers.org/data_models/genealogy/index.htm)

---
---
---

## be-coding-challenge

### Expectations

- We do not expect you to completely finish the challenge. We ask that candidates spend 4 hours or more working through the challenge. With that we understand that everyones schedule and availability is different so we ask that you provide a reasonable estimate of your time commitment so we can take it into account when evaluating your submission.
- We expect you to leverage creative license where it makes sense. If you'd like to change the project structure, pull in libraries, or make assumptions about the requirements we openly encourage you to do so. All that we ask is that you are prepared to talk about your choices in future interviews.

### Challenge

For this challenge you will be implementing a family tree API.

The API should be capable of keeping track of people and the connections between them.

While you have full control to model the entities as you see fit you should keep the following guidelines in mind.

Details about a person and their relationships should be editable. At a minimum you should use the following traits to describe a person:

- First name
- Last name
- Phone number
- Email address (unique)
- Address
- Birth date

When thinking about relations between people the API should be able to provide the following information

- For a given person list all of their siblings
- For a given person list all of their parents
- For a given person list all their children
- For a given person list all of their grandparents
- For a given person list all of their cousins

### Getting started

##### Running the service in a virtual environment

If you are using python 3.7 you will need to run
```bash
pipenv run pip install pip==18.0
```

To install dependencies you will need to run
```bash
pipenv install
```

Once dependencies are installed you can run the service with
```bash
pipenv run python manage.py
```
or
```bash
pipenv shell
python server.py
```
