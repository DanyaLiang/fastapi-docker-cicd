from fastapi import FastAPI
import os
import psycopg2 

app = FastAPI()

@app.get("/")
def read_root():
    # Простая проверка соединения с базой
    status = "Disconnected"
    try:
        # Пытаемся подключиться к базе 'db'
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        status = "Подключено к Postgres"
        conn.close()
    except Exception as e:
        status = f"Error: {e}"

    return {
        "message": "Несколько сервисов работают вместе",
        "db_status": status
    }