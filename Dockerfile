# Використовуємо базовий образ Python
FROM python:3.9-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файл вимог (requirements.txt) у робочу директорію
COPY requirements.txt .

# Встановлюємо залежності з файлу requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код програми в робочу директорію
COPY . .

# Визначаємо команду для запуску програми
CMD ["python", "app.py"]
