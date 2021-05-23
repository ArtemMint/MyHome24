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
init: up update-db
reboot: down up
up: docker-build docker-up docker-prune
down: docker-down
update-db: docker-migrations docker-migrate

# Simple commands
docker-build:
	docker-compose build
docker-up:
	docker-compose up -d
docker-down:
	docker-compose down
docker-stop:
	docker-compose stop
docker-prune:
	docker image prune -f
docker-migrations:
	docker-compose exec django ./manage.py makemigrations
docker-migrate:
	docker-compose exec django ./manage.py migrate

docker-shell:
	docker-compose exec django ./manage.py shell
