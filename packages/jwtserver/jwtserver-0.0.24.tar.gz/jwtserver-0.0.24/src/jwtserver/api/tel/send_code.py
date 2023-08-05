from fastapi import Body, Depends, HTTPException
from redis import Redis
from starlette import status

from jwtserver.api.api_v1.endpoints.reg.routers import router_api_v1_reg
from jwtserver.api.api_v1.endpoints.reg.types_model import RespSendCodeModel
from jwtserver.dependencies.init_redis import redis_conn
from jwtserver.internal.SMSCRules import SMSRules
from jwtserver.settings import Settings, get_settings


@router_api_v1_reg.post(
    "/send_code",
    response_model=RespSendCodeModel,
    description="Sending a code through a call or SMS",
    name="reg:send_code",
)
async def send_code(
    telephone: str = Body(...),
    settings: Settings = Depends(get_settings),
    redis: Redis = Depends(redis_conn),
):
    sms_rules = SMSRules(settings, redis)
    result = await sms_rules.send_code(telephone)

    if result.error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "error": result.error,
                "block_time": result.error.details.block_time,
            },
        )

    return {
        "send": True,
        "block_time": result.is_sent.block_time.timestamp(),
        "method": result.is_sent.method,
    }
