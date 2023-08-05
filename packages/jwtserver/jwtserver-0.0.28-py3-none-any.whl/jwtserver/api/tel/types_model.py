from pydantic import BaseModel


class CheckCodeResponseModel(BaseModel):
    reg_token: str


class PhoneStatusModel(BaseModel):
    free: bool
    telephone: str


class RespError(BaseModel):
    error: str
    block_time: int | None


class RespSendCodeModel(BaseModel):
    send: bool
    block_time: float
    method: str


class Data(BaseModel):
    telephone: str
    password: str
    reg_token: str


class AccessTokenResponseModel(BaseModel):
    access_token: str
    token_type: str
