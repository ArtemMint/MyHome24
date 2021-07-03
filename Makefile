# Docker
# Complex commands
init: up update-db
reboot: down up
up: docker-build docker-up docker-prune
down: docker-down
update-db: docker-migrations docker-migrate
collectstatic: docker-collectstatic
tests: docker-test-admin-panel docker-test-register

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
	docker-compose exec django ./manage.py makemigrations --no-input
docker-migrate:
	docker-compose exec django ./manage.py migrate --no-input
docker-shell:
	docker-compose exec django ./manage.py shell
docker-collectstatic:
	docker-compose exec django ./manage.py collectstatic --no-input
docker-test-register:
	docker-compose exec django ./manage.py test register
docker-test-admin-panel:
	docker-compose exec django ./manage.py test admin_panel