.PHONY: bootstrap install test serve all

bootstrap:
	curl https://bootstrap.pypa.io/get-pip.py | python3
	pip3 install poetry

install-dev:
	poetry install 

install:
	poetry install --no-dev

serve:
	poetry run gunicorn -c deploy/wsgi/guconfig.py refwebapp.wsgi

test:
	poetry run pytest
