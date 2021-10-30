web: gunicorn -c gunicorn-conf.py EmailSender.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate