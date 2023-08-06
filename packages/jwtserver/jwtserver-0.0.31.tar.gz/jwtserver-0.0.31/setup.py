# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jwtserver',
 'jwtserver.api',
 'jwtserver.api.api_v1',
 'jwtserver.api.api_v1.endpoints',
 'jwtserver.api.tel',
 'jwtserver.core',
 'jwtserver.crud',
 'jwtserver.db',
 'jwtserver.dependencies',
 'jwtserver.functions',
 'jwtserver.help_func',
 'jwtserver.internal',
 'jwtserver.migration',
 'jwtserver.migration.versions',
 'jwtserver.models',
 'jwtserver.recaptcha',
 'jwtserver.schemas',
 'jwtserver.tests']

package_data = \
{'': ['*'], 'jwtserver': ['email-templates/build/*', 'email-templates/src/*']}

install_requires = \
['alembic>=1.10.2,<2.0.0',
 'asyncpg==0.27.0',
 'celery>=5.2.7,<6.0.0',
 'emails>=0.6,<0.7',
 'fastapi>=0.94.1,<0.95.0',
 'httpx>=0.23.3,<0.24.0',
 'loguru>=0.6.0,<0.7.0',
 'passlib==1.7.4',
 'phonenumbers>=8.13.7,<8.14.0',
 'psycopg2==2.9.5',
 'pydantic[email]>=1.10.6,<2.0.0',
 'pytest==7.2.2',
 'python-dotenv>=1.0.0,<2.0.0',
 'python-jose[cryptography]>=3.3.0,<4.0.0',
 'python-multipart>=0.0.6,<0.0.7',
 'redis[hiredis]>=4.5.1,<5.0.0',
 'setuptools>=67.6.0,<67.7.0',
 'sqlalchemy>=2.0.6,<2.1.0',
 'sqlalchemy_utils>=0.40.0,<0.41.0',
 'starlette>=0.26.1,<0.27.0',
 'uvicorn>=0.21.1,<0.22.0']

entry_points = \
{'console_scripts': ['updatehead = jwtserver.commands:db_upgrade_cmd']}

setup_kwargs = {
    'name': 'jwtserver',
    'version': '0.0.31',
    'description': 'jwt authorization server',
    'long_description': '# JWT server\n\n_JWTServer лёгкий и быстрый микросервис JWT._\n\n[![Package version](https://img.shields.io/pypi/v/jwtserver?color=%2334D058&label=pypi%20package)](https://pypi.org/project/jwtserver)\n[![Supported Python versions](https://img.shields.io/pypi/pyversions/jwtserver.svg?color=%2334D058)](https://pypi.org/project/jwtserver)\n\nJWT Server является микросервисом для авторизации пользователей. Имеющий гибкие настройки и разные версии API.\n\n## Особенности\n\n* Быстрый старт\n* Идеален для тестирования frontend\n* Спецификация JWT токенов\n* Основан на Fast API framework\n* Постоянная поддержка\n\n---\n\n**Документация** <a href="https://jwtserver.goltsev.net/" target="_blank">https://jwtserver.goltsev.net/</a>\n\n**Поддержка кода** <a href="https://github.com/goltsevnet/jwtserver" target="_blank">https://github.com/goltsevnet/jwtserver</a>\n\n---\n\n## Зависимости\n\n* **uvicorn** <a href="https://www.uvicorn.org/" target="_blank" class="external-link">https://www.uvicorn.org/</a>\n* **fastapi** <a href="https://fastapi.tiangolo.com/" target="_blank" class="external-link">https://fastapi.tiangolo.com/</a>\n* **starlette** <a href="https://www.starlette.io/" target="_blank" class="external-link">https://www.starlette.io/</a>\n* **passlib** <a href="https://pypi.org/project/passlib/" target="_blank" class="external-link">https://pypi.org/project/passlib/</a>\n* **pydantic** <a href="https://pydantic-docs.helpmanual.io/" target="_blank" class="external-link">https://pydantic-docs.helpmanual.io/</a>\n* **redis** <a href="https://pypi.org/project/redis/" target="_blank" class="external-link">https://pypi.org/project/redis/</a>\n* **python-jose** <a href="https://pypi.org/project/python-jose/" target="_blank" class="external-link">https://pypi.org/project/python-jose/</a>\n* **sqlalchemy** <a href="https://pypi.org/project/SQLAlchemy/" target="_blank" class="external-link">https://pypi.org/project/SQLAlchemy/</a>\n* **sqlalchemy_utils** <a href="https://sqlalchemy-utils.readthedocs.io/" target="_blank" class="external-link">https://sqlalchemy-utils.readthedocs.io/</a>\n* **asyncpg** <a href="https://pypi.org/project/asyncpg/" target="_blank" class="external-link">https://pypi.org/project/asyncpg/</a>\n* **psycopg2-binary** <a href="https://pypi.org/project/psycopg2-binary/" target="_blank" class="external-link">https://pypi.org/project/psycopg2-binary/</a>\n* **httpx** <a href="https://www.python-httpx.org/" target="_blank" class="external-link">https://www.python-httpx.org/</a>\n* **python-dotenv** <a href="https://pypi.org/project/python-dotenv/" target="_blank" class="external-link">https://pypi.org/project/python-dotenv/</a>\n\n## Установка\n\n```shell\npython -m pip install jwtserver \n```\n\n## Примеры:\n\n### Для разработки\n\n* создайте файл `dev.py`\n\n```python\nfrom jwtserver.server import dev\n\nif __name__ == "__main__":\n    dev(host="localhost", port=5000, log_level="info")\n```\n\n### Интерактивная API документация\n\nоткройте _Interactive API docs_ <a href="http://localhost:5000/docs" target="_blank" class="external-link">http://localhost:5000/docs</a>\n\nВы увидите автоматическую интерактивную документацию по API.\n\n### Альтернативная API документация\n\nоткройте _Alternative  API redoc_ <a href="http://localhost:5000/redoc" target="_blank" class="external-link">http://localhost:5000/redoc</a>\n\n### Для продукции\n\n* создайте файл `main.py`\n\n```python\nfrom jwtserver.app import app\n\napp.debug = False\n```\n\n## Лицензия\nЭтот проект находится под лицензией Apache 2.0.\n',
    'author': 'darkdealnet',
    'author_email': 'real@darkdeal.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
