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


## Alembic

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

