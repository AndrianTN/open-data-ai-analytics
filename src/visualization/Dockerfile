FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/visualization/ ./src/visualization/
COPY data/ ./data/
# Переконайся, що ім'я файлу (тут visualization.py) відповідає твоєму
CMD ["python", "src/visualization/visualization.py"]