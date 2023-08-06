# Import all the models, so that Base has them before being
# imported by Alembic
from jwtserver.db.base_class import Base  # noqa
from jwtserver.models.item import Item  # noqa
from jwtserver.models.user import User  # noqa
