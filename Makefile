# Django
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

# Docker
docker-build:
	docker build --tag myhome24 .
docker-run:
	docker run --publish 8000:8000 myhome24