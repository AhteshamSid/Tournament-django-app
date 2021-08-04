release: python manage.py migrate
web: gunicorn fixtureapp.wsgi:application --log-file -
