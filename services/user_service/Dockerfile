FROM python:3.11-slim

WORKDIR /app

COPY services/user_service/app/ ./app/
COPY libs/ ./libs/
COPY requirements.txt ./requirements.txt
COPY alembic.ini ./alembic.ini
COPY alembic/ ./alembic/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
