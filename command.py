####################### Python #############################

# # Command to create a virtual environment in MAC
# python3 -m venv .venv

# # Command to activate the virtual environment in MAC
# source .venv/bin/activate

# # Command to install FastAPI and Uvicorn in the virtual environment
# pip install fastapi uvicorn


# # Command to deactivate the virtual environment
# deactivate

# # Command to automatically create a requirements.txt file with the installed packages
# pip freeze > requirements.txt

# # Command to install packages from requirements.txt
# pip install -r requirements.txt

# # Command to check the installed packages in the virtual environment
# pip list

# # Command to remove the virtual environment
# rm -rf .venv

# # Command to start the FastAPI application
# uvicorn main:app --reload


################# Alembic Commands #####################

# Command to initialize Alembic
# alembic init alembic

# Command to create a new migration scripte (make migrations)
# alembic revision --autogenerate -m "Initial migration"

# Command to apply migrations (migrate)
# alembic upgrade head

# Command to downgrade migrations
# alembic downgrade -1

# Command to show the current migration status
# alembic current

# alembic history




############## Docker + Alembic Commands #####################

# Command to initialize Alembic
# docker-compose run --rm fastapi alembic init alembic

# Command to create a new migration script (make migrations)
# docker-compose run --rm fastapi alembic revision --autogenerate -m "Initial migration"

# Command to apply migrations (migrate)
# docker-compose run --rm fastapi alembic upgrade head

# Command to downgrade migrations
# docker-compose run --rm fastapi alembic downgrade -1

# Command to show the current migration status
# docker-compose run --rm fastapi alembic current

# Command to show the migration history
# docker-compose run --rm fastapi alembic history

# Command to make migrations
# docker-compose exec fastapi alembic revision --autogenerate -m "Initial migration"

# Command to apply migrations (migrate)
# docker-compose exec fastapi alembic upgrade head


############## Docker Commands #####################

# Command to build the Docker images
# docker-compose build

# Command to start the Docker containers
# docker-compose up -d
# docker-compose -f docker-compose-dev.yml up -d
# docker-compose -f docker-compose-prod.yml up -d

# Command to stop the Docker containers
# docker-compose down
# docker-compose -f docker-compose-dev.yml down
# docker-compose -f docker-compose-prod.yml down

# Command to view the logs of a specific service
# docker-compose logs <service_name>

# Command to execute a command inside a running container
# docker-compose exec <service_name> <command>

# Command to list all running containers
# docker ps

# Command to list all containers (including stopped ones)
# docker ps -a

# Command to view the logs of a specific container
# docker logs <container_id>

# Command to view the logs of a specific service
# docker-compose logs <service_name>

# Command to show running containers
# docker ps



############## Pytest Commands #####################

# Command to run all tests
# pytest

# Command to run a specific test file
# pytest tests/test_users.py

# Command to run a specific test function
# pytest tests/test_users.py::test_create_user_success

# Command to show detailed test output
# pytest -v

# Command to show test output in real-time
# pytest -s

# Command to run tests with a specific marker
# pytest -m "marker_name"

# Command to generate a test report
# pytest --html=report.html

# Command to run tests with coverage
# pytest --cov=app tests/

# Command to disable warnings
# pytest -p no:warnings

# Command to stop pytest as soon as a failure occurs
# pytest --maxfail=1

# Command to run tests in a specific directory
# pytest tests/


# Command to enter user service container
# docker compose -f infra/docker-compose.yml exec user_service bash