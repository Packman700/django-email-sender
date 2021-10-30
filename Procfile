web: gunicorn EmailSender.wsgi --log-file -
python manage.py migrate
worker: python manage.py qcluster