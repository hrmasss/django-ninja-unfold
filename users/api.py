from ninja_jwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from common.schema import MessageSchema
from http import HTTPStatus
from ninja import Router
from typing import Any
from users.schema import (
    TokenRequestSchema,
    TokenSchema,
    TokenVerifySchema,
    TokenRefreshSchema,
    UserSchema,
)


router = Router(tags=["Authentication"])


@router.post(
    "/token",
    auth=None,
    summary="Obtain JWT token pair",
    response={HTTPStatus.OK: TokenSchema, HTTPStatus.UNAUTHORIZED: MessageSchema},
)
def create_token(request, payload: TokenRequestSchema) -> Any:
    """
    Create a new token pair (access + refresh) for valid credentials.
    """
    user = authenticate(username=payload.username, password=payload.password)
    if not user or not user.is_active:
        return HTTPStatus.UNAUTHORIZED, {"message": "Invalid credentials"}

    refresh = RefreshToken.for_user(user)
    return HTTPStatus.OK, {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "token_type": "Bearer",
    }


@router.post(
    "/token/verify",
    auth=None,
    summary="Verify access token",
    response={HTTPStatus.OK: MessageSchema, HTTPStatus.UNAUTHORIZED: MessageSchema},
)
def verify_token(request, payload: TokenVerifySchema) -> Any:
    """
    Verify if an access token is valid.
    """
    try:
        AccessToken(payload.access)
        return HTTPStatus.OK, {"message": "Token is valid"}
    except Exception:
        return HTTPStatus.UNAUTHORIZED, {"message": "Invalid or expired token"}


@router.post(
    "/token/refresh",
    auth=None,
    summary="Refresh access token",
    response={HTTPStatus.OK: TokenSchema, HTTPStatus.UNAUTHORIZED: MessageSchema},
)
def refresh_token(request, payload: TokenRefreshSchema) -> Any:
    """
    Create new token pair using a valid refresh token.
    """
    try:
        refresh = RefreshToken(payload.refresh)
        return HTTPStatus.OK, {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "token_type": "Bearer",
        }
    except Exception:
        return HTTPStatus.UNAUTHORIZED, {"message": "Invalid or expired refresh token"}


@router.post(
    "/token/revoke",
    summary="Revoke refresh token",
    response={HTTPStatus.OK: MessageSchema, HTTPStatus.UNAUTHORIZED: MessageSchema},
)
def revoke_token(request, payload: TokenRefreshSchema) -> Any:
    """
    Revoke a refresh token (logout).
    """
    try:
        refresh = RefreshToken(payload.refresh)
        refresh.blacklist()
        return HTTPStatus.OK, {"message": "Token successfully revoked"}
    except Exception:
        return HTTPStatus.UNAUTHORIZED, {"message": "Invalid token"}


@router.get(
    "/users/me",
    summary="Get authenticated user",
    response={HTTPStatus.OK: UserSchema, HTTPStatus.UNAUTHORIZED: MessageSchema},
)
def get_current_user(request) -> Any:
    """
    Retrieve the authenticated user's profile.
    """
    user = request.auth
    return HTTPStatus.OK, {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "roles": [role.name for role in user.roles.all()],
    }
