from secrets import token_hex

from fastapi import Body, Depends, HTTPException
from jwtserver.api.api_v1.endpoints.reg.routers import router_api_v1_reg
from jwtserver.api.api_v1.endpoints.reg.types_model import CheckCodeResponseModel
from redis import Redis
from starlette import status

from jwtserver.dependencies.init_redis import redis_conn
from jwtserver.recaptcha.Recaptcha_v3 import Recaptcha


@router_api_v1_reg.post(
    "/check_code",
    description="User authorization by login and password",
    # response_description=response_description,
    response_model=CheckCodeResponseModel,
)
async def check_code(
    # redis: Redis,
    telephone: str = Body(...),
    code: int = Body(...),
    redis: Redis = Depends(redis_conn),
    recaptcha: Recaptcha = Depends(Recaptcha),
):
    """Checking the code from SMS or Call
    :param str telephone: Telephone number in international format
    :param int code: 4 digit verification code
    :param redis: Redis client
    :param recaptcha: Validate Google recaptcha_v3.md v3 [return True or HTTPException]
    :return: one-time token for registration
    """
    await recaptcha.set_action_name("SignUpPage/CheckCode").greenlight()

    code_method = redis.get(telephone)
    if code_method:
        from_redis_code, method = code_method.split(":")
        if int(from_redis_code) == code:
            reg_token = token_hex(16)
            redis.set(f"{telephone}_reg_token", reg_token, 60 * 60)
            return {"reg_token": reg_token}

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Неверный код",
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Нужно запросить новый код ",
    )
