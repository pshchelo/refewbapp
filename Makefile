.PHONY: bootstrap install test gunicorn uwsgi

bootstrap:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

install-dev:
	poetry install 

install-prod:
	POETRY_VIRTUALENVS_CREATE=false poetry install --no-dev

gunicorn:
	poetry run gunicorn -c deploy/wsgi/guconfig.py refwebapp.wsgi

uwsgi:
	poetry run uwsgi --ini deploy/wsgi/uwsgi.ini

test:
	poetry run pytest
