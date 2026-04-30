import pandas as pd
import sqlite3
import os

print("--- Module: Data Load ---")


csv_path = "data/raw/passengers.csv"


db_path = "data/database.db"


if not os.path.exists(csv_path):
    print("CSV файл не знайдено!")
    exit(1)


df = pd.read_csv(csv_path)
print(f"CSV завантажено. Кількість рядків: {len(df)}")


conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    month INTEGER,
    branch TEXT,
    passengers INTEGER
)
""")

print("Таблиця створена або вже існує")


cursor.execute("DELETE FROM passengers")


df.to_sql("passengers", conn, if_exists="append", index=False)

print("Дані успішно записані в БД")


conn.commit()
conn.close()

print("Data Load завершено")