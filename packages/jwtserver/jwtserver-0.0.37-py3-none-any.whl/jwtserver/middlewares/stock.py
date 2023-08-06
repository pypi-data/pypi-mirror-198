from fastapi import Request

# TODO: middleware stock


async def middleware_stock(request: Request, call_next):
    response = await call_next(request)
    return response
