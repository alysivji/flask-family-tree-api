db:
	pipenv run python initdb.py

up:
	pipenv run python manage.py

shell:
	pipenv run ipython -i scripts/shell.py

test:
	pipenv run pytest
