FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/web/ ./src/web/
COPY reports/ ./reports/

RUN mkdir -p src/web/static && \
    cp reports/figures/passengers_by_branch.png src/web/static/passengers_by_branch.png && \
    cp reports/figures/passengers_by_year.png src/web/static/passengers_by_year.png

CMD ["python", "src/web/app.py"]