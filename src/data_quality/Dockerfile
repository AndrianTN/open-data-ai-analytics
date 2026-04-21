FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/data_quality/ ./src/data_quality/
COPY data/ ./data/
CMD ["python", "src/data_quality/quality_check.py"]