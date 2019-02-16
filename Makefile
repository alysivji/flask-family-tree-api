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
