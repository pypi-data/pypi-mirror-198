from fastapi import Body, Depends
from jwtserver.api.api_v1.endpoints.reg.routers import router_api_v1_reg
from jwtserver.api.api_v1.endpoints.reg.types_model import PhoneStatusModel
from jwtserver.settings import Settings, get_settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from jwtserver.dependencies.session_db import async_db_session
from jwtserver.models import User
from jwtserver.recaptcha.Recaptcha_v3 import Recaptcha

router_kwargs = {"response_model": PhoneStatusModel, "name": "reg:phone_status"}


@router_api_v1_reg.post("/phone_status", **router_kwargs)
async def phone_status(
    telephone: str = Body(...),
    recaptcha_token: str = Body(...),
    session: AsyncSession = Depends(async_db_session),
    settings: Settings = Depends(get_settings),
):
    recaptcha = Recaptcha(
        _config=settings.Google.Recaptcha,
        environment=settings.environment,
        recaptcha_token=recaptcha_token,
    )
    await recaptcha.set_action_name("SignUpPage/PhoneStatus").greenlight()
    stmt = select(User).where(User.telephone == telephone)
    result = session.execute(stmt)
    busy = result.scalars().first()
    return {"free": False if busy else True, "telephone": telephone}
