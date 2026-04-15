import os

def load_data():
    print("--- Module: Data Load ---")
    os.makedirs('data/raw', exist_ok=True)
    print("Папка data/raw готова для завантаження файлів.")

if __name__ == "__main__":
    load_data()