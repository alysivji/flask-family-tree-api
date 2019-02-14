db:
	pipenv run python manage_initdb.py

up:
	pipenv run python manage.py

test:
	pipenv run pytest
