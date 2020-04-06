FROM python:3.6-alpine
ADD . /opt/app
WORKDIR /opt/app
RUN apk add git && pip3 install --no-cache .[mysql,pgsql,serve]
ENTRYPOINT gunicorn -c gunicorn.conf.py "refwebapp.app:create_app()"
