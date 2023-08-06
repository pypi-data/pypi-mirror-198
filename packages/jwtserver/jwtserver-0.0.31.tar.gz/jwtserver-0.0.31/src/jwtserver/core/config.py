from typing import Optional, Dict, Any

from pydantic import BaseSettings, BaseModel, RedisDsn, PostgresDsn, validator, EmailStr

from jwtserver.internal.SMSC import SMSModel


class TokenModel(BaseModel):
    base_sol: str = "1234567890987654321"
    secret_key: str = None
    algorithm: str = "HS256"
    # 60 minutes * 24 hours * 8 days = 7 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    REFRESH_EXPIRE_TIME: int = 10800  # minutes


class PostgresConfig(BaseModel):
    # password: str = "example"
    # user: str = "postgres"
    # db: str = "postgres"
    # server: str = "localhost"
    # port: int = 5432
    dsn: Optional[PostgresDsn] = None
    # f"postgresql+psycopg2://{user}:{password}@{server}:{port}/{db}"

    @validator("dsn", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            user=values.get("user"),
            password=values.get("password"),
            host=values.get("server"),
            port=values.get("port"),
            path=f"/{values.get('db') or ''}",
        )


class RedisConfig(BaseModel):
    redis_dsn: RedisDsn = None
    max_connections: int = 10


class RecaptchaModel(BaseModel):
    secret_key: str = "uudud"
    score: float = 0.7
    for_tests: bool = False


class GoogleConfig(BaseModel):
    Recaptcha: RecaptchaModel = RecaptchaModel()


class ServerConfig(BaseModel):
    # domain: Set[str] = set()
    host: str = "0.0.0.0"
    port: int = 8000
    max_requests: int = 1000
    debug: bool = True


class SMTPConfig(BaseModel):
    tls: bool = True
    port: Optional[int] = None
    host: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None


class EmailsConfig(BaseModel):
    from_email: Optional[EmailStr] = None
    from_name: Optional[str] = None

    @validator("from_name")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )


class Settings(BaseSettings):
    environment: str = "production"
    server: ServerConfig = ServerConfig()
    token: TokenModel = TokenModel()
    postgres: PostgresConfig = PostgresConfig()
    smtp: SMTPConfig = SMTPConfig()
    redis: RedisConfig = RedisConfig()
    Google: GoogleConfig = GoogleConfig()
    sms: SMSModel = SMSModel()
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"


settings = Settings()
