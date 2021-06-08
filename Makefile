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
docker-collectstatic:
	docker-compose exec django ./manage.py collectstatic