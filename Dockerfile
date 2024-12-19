# Используем официальный Python 3.12.4 slim образ
FROM python:3.12.4-slim

# Установим рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /app/

# Устанавливаем переменную окружения для Django
ENV PYTHONUNBUFFERED 1

# Порты, которые будет использовать приложение
EXPOSE 8000

# Команда для запуска приложения
#CMD ["gunicorn", "puddle.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]