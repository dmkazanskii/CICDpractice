# Установка Python из официального базового образа
FROM python:3.9-slim

# Добавляем метаданные
LABEL maintainer="dmkazanskii@yandex.ru"
LABEL version="v3.0"
LABEL description="Port:8180 app2:10 msg break"

# Установка рабочей директории внутри будущего контейнера
WORKDIR /app
# Копирование всех файлов приложения в контейнер
COPY app2.py /app
# Экспорт порта, на котором будет работать приложение
EXPOSE 8180
# Запуск тестового Python-приложения
CMD ["python", "app2.py"]