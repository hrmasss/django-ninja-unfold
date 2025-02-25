from typing import List
from ninja import Schema


class TokenSchema(Schema):
    access: str
    refresh: str
    token_type: str = "Bearer"


class TokenRequestSchema(Schema):
    username: str
    password: str


class TokenVerifySchema(Schema):
    access: str


class TokenRefreshSchema(Schema):
    refresh: str


class UserSchema(Schema):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    roles: List[str]
