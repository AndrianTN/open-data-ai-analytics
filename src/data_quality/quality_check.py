import pandas as pd
import sqlite3
import json
import os

print("--- Module: Data Quality Check ---")

db_path = "data/database.db"
report_path = "reports/quality_report.json"

if not os.path.exists(db_path):
    print("БД не знайдена! Спочатку запусти data_load")
    exit(1)


conn = sqlite3.connect(db_path)

df = pd.read_sql("SELECT * FROM passengers", conn)

print(f" Завантажено {len(df)} записів з БД")

missing_values = df.isnull().sum().to_dict()


duplicates = df.duplicated().sum()


data_types = df.dtypes.astype(str).to_dict()


invalid_values = {
    "negative_passengers": int((df["passengers"] < 0).sum()),
    "invalid_month": int(((df["month"] < 1) | (df["month"] > 12)).sum())
}


report = {
    "total_rows": len(df),
    "missing_values": missing_values,
    "duplicates": int(duplicates),
    "data_types": data_types,
    "invalid_values": invalid_values
}


os.makedirs("reports", exist_ok=True)


with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

print("Звіт якості збережено:", report_path)

conn.close()

print("Data Quality завершено")