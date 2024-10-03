FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]
