runserver:
	./manage.py runserver

mm: makemigrations migrate

makemigrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

test_all:
	./manage.py test