# JWT server

_JWTServer лёгкий и быстрый микросервис JWT._

[![Package version](https://img.shields.io/pypi/v/jwtserver?color=%2334D058&label=pypi%20package)](https://pypi.org/project/jwtserver)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/jwtserver.svg?color=%2334D058)](https://pypi.org/project/jwtserver)

JWT Server является микросервисом для авторизации пользователей. Имеющий гибкие настройки и разные версии API.

* Подключение Google Recaptcha V3
* Отправка кода через сервис <a href="https://smsc.ru/" target="_blank">https://smsc.ru/</a> (**стадии тестирования**)

## Особенности

* Быстрый старт
* Походит для тестирования frontend
* Основан на Fast API framework и вдохновлен работами <a href="https://github.com/tiangolo" target="_blank">tiangolo</a>

## Route Entrypoints

### Login
* **[POST]** - /api/v1/login/access-token
* **[POST]** - /api/v1/login/test-token
* **[POST]** - /api/v1/password-recovery/{email}
* **[POST]** - /api/v1/reset-password/
* **[POST]** - /api/v1/phone_status/

### Users
* **[GET]** - /api/v1/users/
* **[POST]** - /api/v1/users/
* **[GET]** - /api/v1/users/me
* **[PUT]** - /api/v1/users/me
* **[POST]** - /api/v1/users/open
* **[GET]** - /api/v1/users/{user_id}
* **[PUT]** - /api/v1/users/{user_id}

### Utils
* **[POST]** - /api/v1/utils/test-celery/
* **[POST]** - /api/v1/utils/test-email/

### Items
* **[GET]** - /api/v1/items/
* **[POST]** - /api/v1/items/
* **[GET]** - /api/v1/items/{id}
* **[PUT]** - /api/v1/items/{id}
* **[DELETE]** - /api/v1/items/{id}

---

**Документация** <a href="https://jwtserver.goltsev.net/" target="_blank">https://jwtserver.goltsev.net/</a>

**Поддержка кода** <a href="https://github.com/goltsevnet/jwtserver" target="_blank">https://github.com/goltsevnet/jwtserver</a>

---

## Зависимости

* **uvicorn** <a href="https://www.uvicorn.org/" target="_blank" class="external-link">https://www.uvicorn.org/</a>
* **fastapi** <a href="https://fastapi.tiangolo.com/" target="_blank" class="external-link">https://fastapi.tiangolo.com/</a>
* **starlette** <a href="https://www.starlette.io/" target="_blank" class="external-link">https://www.starlette.io/</a>
* **passlib** <a href="https://pypi.org/project/passlib/" target="_blank" class="external-link">https://pypi.org/project/passlib/</a>
* **pydantic** <a href="https://pydantic-docs.helpmanual.io/" target="_blank" class="external-link">https://pydantic-docs.helpmanual.io/</a>
* **redis** <a href="https://pypi.org/project/redis/" target="_blank" class="external-link">https://pypi.org/project/redis/</a>
* **python-jose** <a href="https://pypi.org/project/python-jose/" target="_blank" class="external-link">https://pypi.org/project/python-jose/</a>
* **sqlalchemy** <a href="https://pypi.org/project/SQLAlchemy/" target="_blank" class="external-link">https://pypi.org/project/SQLAlchemy/</a>
* **sqlalchemy_utils** <a href="https://sqlalchemy-utils.readthedocs.io/" target="_blank" class="external-link">https://sqlalchemy-utils.readthedocs.io/</a>
* **asyncpg** <a href="https://pypi.org/project/asyncpg/" target="_blank" class="external-link">https://pypi.org/project/asyncpg/</a>
* **psycopg2-binary** <a href="https://pypi.org/project/psycopg2-binary/" target="_blank" class="external-link">https://pypi.org/project/psycopg2-binary/</a>
* **httpx** <a href="https://www.python-httpx.org/" target="_blank" class="external-link">https://www.python-httpx.org/</a>
* **python-dotenv** <a href="https://pypi.org/project/python-dotenv/" target="_blank" class="external-link">https://pypi.org/project/python-dotenv/</a>

## Установка

```shell
python -m pip install jwtserver 
```

## Примеры:

### Для разработки

* создайте файл `dev.py`

```python
from jwtserver.server import dev

if __name__ == "__main__":
    dev(host="localhost", port=5000, log_level="info")
```


### Интерактивная API документация

откройте _Interactive API docs_ <a href="http://localhost:5000/docs" target="_blank" class="external-link">http://localhost:5000/docs</a>

Вы увидите автоматическую интерактивную документацию по API.

### Альтернативная API документация

откройте _Alternative  API redoc_ <a href="http://localhost:5000/redoc" target="_blank" class="external-link">http://localhost:5000/redoc</a>

### Для продукции

* создайте файл `main.py`

```python
from jwtserver.app import app

app.debug = False
```

* **Gunicorn:** `gunicorn main:app`

## Лицензия
Этот проект находится под лицензией Apache 2.0.
