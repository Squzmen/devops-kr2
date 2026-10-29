# devops-kr2

Контрольная работа № 2, вариант 2: Flask-приложение со счётчиком в Redis, опубликованное по адресу https://notes.devops.local.

- `Dockerfile` — образ `kr2-app:1.0` (python:3.12-slim, непривилегированный пользователь, порт 8002);
- `docker-compose.yml` — сервисы `app` и `redis` (redis:7-alpine, пароль, том `redis_data`, сеть `backend`);
- `.env.example` — шаблон секретов; рабочий `.env` создаётся только на сервере (`openssl rand -hex 32`, права 600);
- `deploy/nginx/kr2.conf` — конфигурация обратного прокси `/etc/nginx/sites-available/kr2`.

Запуск на сервере: `docker compose up -d --build`. Порт приложения публикуется только на 127.0.0.1, доступ извне — через Nginx.
