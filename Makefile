run: collectstatic migrations-migrate collectstatic runserver
migrations-migrate: makemigrations migrate

runserver:
	./manage.py runserver

makemigrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

test_all:
	./manage.py test

collectstatic:
	./manage.py collectstatic --no-input

shell:
	./manage.py shell