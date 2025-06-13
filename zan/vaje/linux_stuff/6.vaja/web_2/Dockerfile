FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && \
                apt-get install -y curl && \
                pip install --no-cache-dir flask flask-cors regex

COPY src /app

CMD ["python", "app.py"]

