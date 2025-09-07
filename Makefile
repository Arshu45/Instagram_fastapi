up:
	docker compose -f infra/docker-compose.yml up -d

down:
	docker compose -f infra/docker-compose.yml down

build:
	docker compose -f infra/docker-compose.yml build

logs:
	docker compose -f infra/docker-compose.yml logs -f

test:
	docker compose -f infra/docker-compose.yml exec user_service pytest

format:
	black .

lint:
	flake8 .
