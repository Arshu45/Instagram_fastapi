FROM python:3.11-slim

WORKDIR /app

COPY services/post_service/app/ ./app/
COPY libs/ ./libs/
COPY requirements.txt ./requirements.txt
COPY services/post_service/alembic.ini ./alembic.ini
COPY services/post_service/alembic/ ./alembic/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
