"""Authentication use cases: login and refresh-token revocation on logout."""

from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models import RefreshToken
from app.repositories import user_repository
from app.security.passwords import verify_password
from app.security.tokens import (
    create_access_token,
    generate_refresh_token,
    hash_refresh_token,
)


class AuthError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


def login(db: Session, username: str, password: str) -> dict:
    settings = get_settings()
    user = user_repository.get_user_by_username(db, username)
    if user is None or not verify_password(password, user.password_hash):
        raise AuthError("Invalid username or password.")

    access_token = create_access_token(user.id, user.role)
    refresh_token = generate_refresh_token()
    db.add(
        RefreshToken(
            user_id=user.id,
            token_hash=hash_refresh_token(refresh_token),
            expires_at=datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_DAYS),
        )
    )
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_MINUTES * 60,
        "user": {
            "id": user.id,
            "username": user.username,
            "display_name": user.display_name,
            "role": user.role,
            "preferred_language": user.preferred_language,
        },
    }


def logout(db: Session, user_id: int, refresh_token: str) -> None:
    """Revoke the given refresh token for this user. Idempotent: unknown or already-revoked tokens are ignored."""
    stmt = select(RefreshToken).where(
        RefreshToken.user_id == user_id,
        RefreshToken.token_hash == hash_refresh_token(refresh_token),
        RefreshToken.revoked_at.is_(None),
    )
    token_row = db.scalar(stmt)
    if token_row is None:
        return
    token_row.revoked_at = datetime.now(timezone.utc)
    db.commit()
