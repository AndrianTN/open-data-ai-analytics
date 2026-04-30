from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

QUALITY_REPORT = "reports/quality_report.json"
RESEARCH_REPORT = "reports/research_report.json"

@app.route("/")
def index():
    quality = {}
    research = {}

    if os.path.exists(QUALITY_REPORT):
        with open(QUALITY_REPORT, "r", encoding="utf-8") as f:
            quality = json.load(f)

    if os.path.exists(RESEARCH_REPORT):
        with open(RESEARCH_REPORT, "r", encoding="utf-8") as f:
            research = json.load(f)

    html = """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Open Data AI Analytics</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background: #f5f7fa;
                color: #222;
            }
            h1, h2 {
                color: #1f4e79;
            }
            .card {
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            }
            pre {
                background: #eee;
                padding: 15px;
                border-radius: 8px;
                overflow-x: auto;
            }
            img {
                max-width: 700px;
                width: 100%;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <h1>Open Data AI Analytics</h1>

        <div class="card">
            <h2>Опис проєкту</h2>
            <p>
                Проєкт призначений для аналізу пасажирських перевезень.
                Система завантажує CSV-дані у базу даних, перевіряє їх якість,
                виконує базове дослідження та будує графіки.
            </p>
        </div>

        <div class="card">
            <h2>Результати перевірки якості даних</h2>
            <h3>Кількість записів: {{ quality.total_rows }}</h3>
            <p>Дублікати: {{ quality.duplicates }}</p>

            <h4>Пропуски:</h4>
            <ul>
            {% for key, value in quality.missing_values.items() %}
                <li>{{ key }}: {{ value }}</li>
            {% endfor %}
            </ul>
        </div>

        <div class="card">
            <h2>Результати дослідження</h2>
             <h3>Загальна кількість пасажирів: {{ research.stats.total_passengers }}</h3>
             <p>Середнє: {{ research.stats.average_passengers }}</p>

             <h4>По філіях:</h4>
             <ul>
             {% for key, value in research.by_branch.items() %}
              <li>{{ key }}: {{ value }}</li>
             {% endfor %}
             </ul>
        </div>

        <div class="card">
            <h2>Візуалізації</h2>
            <h3>Кількість пасажирів по філіях</h3>
            <img src="/static/passengers_by_branch.png">

            <h3>Кількість пасажирів по роках</h3>
            <img src="/static/passengers_by_year.png">
        </div>
    </body>
    </html>
    """

    return render_template_string(
        html,
        quality=quality,
        research=research
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)