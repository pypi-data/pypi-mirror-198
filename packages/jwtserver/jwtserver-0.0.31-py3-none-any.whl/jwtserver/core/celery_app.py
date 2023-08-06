from celery import Celery

celery_jwtserver = Celery("worker", broker="amqp://guest@queue//")

celery_jwtserver.conf.task_routes = {"jwtserver.worker.test_celery": "main-queue"}
