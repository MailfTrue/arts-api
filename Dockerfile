FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./Pipfile rPipfile
COPY ./Pipfile.lock Pipfile.lock
# Adds our application code to the image
COPY . code
WORKDIR code

RUN set -ex && pip install -U pipenv
RUN set -ex && pipenv install --deploy --system
RUN python manage.py collectstatic

EXPOSE 8000

# Run the production server
CMD gunicorn --bind 0.0.0.0:$PORT --access-logfile - app.wsgi:application
