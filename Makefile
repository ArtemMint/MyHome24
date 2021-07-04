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
	cd docker && docker-compose build
docker-up:
	cd docker && docker-compose up -d
docker-down:
	cd docker && docker-compose down
docker-stop:
	cd docker && docker-compose stop
docker-prune:
	cd docker && docker image prune -f
docker-migrations:
	cd docker && docker-compose exec django ./manage.py makemigrations --no-input
docker-migrate:
	cd docker && docker-compose exec django ./manage.py migrate --no-input
docker-shell:
	cd docker && docker-compose exec django ./manage.py shell
docker-collectstatic:
	cd docker && docker-compose exec django ./manage.py collectstatic --no-input
docker-test-register:
	cd docker && docker-compose exec django ./manage.py test register
docker-test-admin-panel:
	cd docker && docker-compose exec django ./manage.py test admin_panel