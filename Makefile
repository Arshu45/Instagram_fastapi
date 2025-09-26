# Docker Compose Commands
up:
	docker compose -f infra/docker-compose.yml up -d

down:
	docker compose -f infra/docker-compose.yml down

build:
	docker compose -f infra/docker-compose.yml build

logs:
	docker compose -f infra/docker-compose.yml logs -f

logs-user:
	docker compose -f infra/docker-compose.yml logs -f user_service

logs-post:
	docker compose -f infra/docker-compose.yml logs -f post_service

logs-db:
	docker compose -f infra/docker-compose.yml logs -f postgres

# Service Management
restart:
	docker compose -f infra/docker-compose.yml restart

restart-user:
	docker compose -f infra/docker-compose.yml restart user_service

restart-post:
	docker compose -f infra/docker-compose.yml restart post_service

# Database Commands
migrate-user:
	docker compose -f infra/docker-compose.yml exec user_service alembic upgrade head

migrate-post:
	docker compose -f infra/docker-compose.yml exec post_service alembic upgrade head

migrate:
	$(MAKE) migrate-user
	$(MAKE) migrate-post

# Testing
test:
	pytest

test-user:
	docker compose -f infra/docker-compose.yml exec user_service pytest

test-post:
	docker compose -f infra/docker-compose.yml exec post_service pytest

# Code Quality
format:
	black .

lint:
	flake8 .

# Development Helpers
shell-user:
	docker compose -f infra/docker-compose.yml exec user_service bash

shell-post:
	docker compose -f infra/docker-compose.yml exec post_service bash

shell-db:
	docker compose -f infra/docker-compose.yml exec postgres psql -U instagram

# Cleanup
clean:
	docker compose -f infra/docker-compose.yml down -v
	docker system prune -f

# Status
status:
	docker compose -f infra/docker-compose.yml ps

# Health Check
health:
	@echo "Checking service health..."
	@curl -s http://localhost:8000/health || echo "User service: DOWN"
	@curl -s http://localhost:8001/health || echo "Post service: DOWN"
	@echo "pgAdmin: http://localhost:5050"
	@echo "PostgreSQL: localhost:5432"

# Quick Start
dev: build up migrate
	@echo "Development environment ready!"
	@echo "User Service: http://localhost:8000"
	@echo "Post Service: http://localhost:8001"
	@echo "pgAdmin: http://localhost:5050"
