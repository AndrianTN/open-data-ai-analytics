
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY src/data_load/ ./src/data_load/
COPY data/ ./data/


CMD ["python", "src/data_load/load.py"]