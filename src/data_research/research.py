import pandas as pd
import sqlite3
import json
import os

print("--- Module: Data Research ---")

db_path = "data/database.db"
report_path = "reports/research_report.json"

if not os.path.exists(db_path):
    print("БД не знайдена! Спочатку запусти data_load")
    exit(1)

conn = sqlite3.connect(db_path)

df = pd.read_sql("SELECT * FROM passengers", conn)

print(f"Завантажено {len(df)} записів")

stats = {
    "total_passengers": int(df["passengers"].sum()),
    "average_passengers": float(df["passengers"].mean()),
    "max_passengers": int(df["passengers"].max()),
    "min_passengers": int(df["passengers"].min())
}


by_branch = df.groupby("branch")["passengers"].sum().to_dict()


by_year = df.groupby("year")["passengers"].sum().to_dict()


report = {
    "stats": stats,
    "by_branch": by_branch,
    "by_year": by_year
}

os.makedirs("reports", exist_ok=True)

with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)
print("Звіт дослідження збережено:", report_path)

conn.close()

print("Data Research завершено")