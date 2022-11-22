# FastAPI CRUD

Данное веб-приложение позволяет производить различные операции с базой данных, например такие, как: поиск по id, удаление, изменение, создание.
В этом проекте задействованы такие технологии, как:

 - Python 3.11 
 - FastAPI 
 - PostgreSQL 
 - Docker/Docker-compose

# Инструкция по поднятию

Скачать данный репозиторий:

    git clone https://github.com/BondarenkoDV/FastAPI_CRUD.git

Ввести следующие команды в терминал:

    docker-compose build
    docker-compose up -d
Дождаться укачивания и распаковки.
FastAPI выдаст ошибку, что не может подключиться к серверу. (Так и должно быть).
Перейти на [127.0.0.1:5050](127.0.0.1:5050), затем создать сервер со следующими входными данными:

> DB_USER=postgres
> 
> DB_PASSWORD=password
> 
> DB_NAME=fastapi_db
> 
> PGADMIN_EMAIL=admin@admin.com
> 
> PGADMIN_PASSWORD=admin

Запустите файл converter.py, чтобы импортировать данные и csv файла в PostgreSQL.

    python3 converter.py


Далее перезапустите docker:

    docker-compose restart
