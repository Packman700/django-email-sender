release: python manage.py migrate
web: gunicorn EmailSender.wsgi --log-file -
worker: python manage.py qcluster
