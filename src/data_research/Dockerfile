FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/data_research/ ./src/data_research/
COPY data/ ./data/
# Переконайся, що ім'я файлу (тут research.py) відповідає твоєму
CMD ["python", "src/data_research/research.py"]