import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

print("--- Module: Visualization ---")

db_path = "data/database.db"
figures_dir = "reports/figures"

if not os.path.exists(db_path):
    print("БД не знайдена! Спочатку запусти data_load")
    exit(1)

os.makedirs(figures_dir, exist_ok=True)

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM passengers", conn)
conn.close()

print(f"Завантажено {len(df)} записів для візуалізації")

branch_data = df.groupby("branch")["passengers"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
branch_data.plot(kind="bar")
plt.title("Кількість пасажирів по філіях")
plt.xlabel("Філія")
plt.ylabel("Кількість пасажирів")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(f"{figures_dir}/passengers_by_branch.png")
plt.close()

print("Збережено графік: passengers_by_branch.png")


year_data = df.groupby("year")["passengers"].sum()

plt.figure(figsize=(8, 5))
year_data.plot(kind="bar")
plt.title("Кількість пасажирів по роках")
plt.xlabel("Рік")
plt.ylabel("Кількість пасажирів")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{figures_dir}/passengers_by_year.png")
plt.close()

print("Збережено графік: passengers_by_year.png")

print("Visualization завершено")