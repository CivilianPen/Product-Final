# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем необходимые зависимости для компиляции
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libevdev-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Команда для выполнения миграций и запуска сервера
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

