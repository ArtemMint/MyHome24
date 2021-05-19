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
# Complex commands
init: docker-build docker-up docker-migrations docker-migrate
reboot: down up
up: docker-build docker-up
down: docker-down

# Simple commands
docker-build:
	docker-compose build
docker-up:
	docker-compose up -d
docker-down:
	docker-compose down
docker-stop:
	docker-compose stop
docker-migrations:
	docker-compose exec web ./manage.py makemigrations
	#docker exec -it myhome24 ./manage.py makemigrations
docker-migrate:
	docker-compose exec web ./manage.py migrate
	#docker exec -it myhome24 ./manage.py migrate
