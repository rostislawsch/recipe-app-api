FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
# this runs the alpine package manager
# and add a package and add the registry
# and do not store the index on our dockerfile
# we wanna minimize the number of extra files 
# included in our docker container
RUN apk add --update --no-cache postgresql-client
# temporary build dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
