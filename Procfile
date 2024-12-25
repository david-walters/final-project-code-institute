web: gunicorn cass_galaar.wsgi
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn cass_galaar.wsgi:application