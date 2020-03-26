.PHONY: bootstrap install test serve

bootstrap:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

install-dev:
	poetry install 

install-prod:
	poetry install --no-dev

serve:
	poetry run gunicorn -c deploy/wsgi/guconfig.py refwebapp.wsgi

test:
	poetry run pytest
