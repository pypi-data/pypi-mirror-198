import os


def upgrade_head():
    os.system("alembic upgrade head")
