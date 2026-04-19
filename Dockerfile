# Берем легкий образ Python
FROM python:3.11-slim

# Указываем рабочую директорию внутри контейнера
WORKDIR /code

# Сначала копируем зависимости, чтобы Docker их кэшировал
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY ./app ./app

# Команда для запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]