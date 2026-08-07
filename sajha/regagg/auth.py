"""
Native signup/login for the on-prem product.

Deliberately dependency-free: scrypt (stdlib hashlib) for password hashing and
an HMAC-signed, expiring session token in an httpOnly cookie. No JWT library,
no bcrypt wheel, nothing to CVE-patch at 2am on a bank's server.

The signing secret comes from REGAGG_SECRET; if unset we generate one at boot
and log a warning — fine for a laptop, flagged loudly for a deployment (sessions
would not survive a restart, which is the point of the warning).
"""

from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
import secrets
import time
from base64 import urlsafe_b64decode, urlsafe_b64encode
from datetime import datetime, timezone
from typing import Optional, Tuple

from sajha.regagg.models import RegUser

logger = logging.getLogger(__name__)

SESSION_COOKIE = "regagg_session"
SESSION_TTL_SECONDS = 12 * 3600          # a working day; re-login after that
_SCRYPT = dict(n=2 ** 14, r=8, p=1, dklen=32)   # ~100ms/hash on a laptop


def _secret() -> bytes:
    env = os.getenv("REGAGG_SECRET")
    if env:
        return env.encode()
    global _EPHEMERAL
    try:
        return _EPHEMERAL
    except NameError:
        _EPHEMERAL = secrets.token_bytes(32)
        logger.warning("REGAGG_SECRET unset — using an ephemeral signing key; "
                       "sessions will not survive a restart. Set it before deploying.")
        return _EPHEMERAL


# ── passwords ───────────────────────────────────────────────────────────────

def hash_password(password: str) -> str:
    """scrypt$<salt_hex>$<hash_hex> — salt per user, parameters pinned above."""
    salt = secrets.token_bytes(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, **_SCRYPT)
    return f"scrypt${salt.hex()}${dk.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        scheme, salt_hex, hash_hex = stored.split("$")
        if scheme != "scrypt":
            return False
        dk = hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt_hex), **_SCRYPT)
        return hmac.compare_digest(dk.hex(), hash_hex)   # constant time
    except Exception:  # noqa: BLE001 — a malformed hash is a failed login, not a 500
        return False


def password_problem(password: str) -> Optional[str]:
    """Return why a password is unacceptable, or None. Length over theatre."""
    if len(password or "") < 10:
        return "Password must be at least 10 characters."
    if password.lower() in {"password123", "changeme12", "letmein1234"}:
        return "That password is too common."
    return None


# ── sessions ────────────────────────────────────────────────────────────────

def _b64(raw: bytes) -> str:
    return urlsafe_b64encode(raw).decode().rstrip("=")


def _unb64(s: str) -> bytes:
    return urlsafe_b64decode(s + "=" * (-len(s) % 4))


def issue_session(user_id: str, ttl: int = SESSION_TTL_SECONDS) -> str:
    payload = json.dumps({"u": user_id, "exp": int(time.time()) + ttl},
                         separators=(",", ":")).encode()
    sig = hmac.new(_secret(), payload, hashlib.sha256).digest()
    return f"{_b64(payload)}.{_b64(sig)}"


def read_session(token: Optional[str]) -> Optional[str]:
    """Return the user_id in a valid, unexpired token — else None."""
    if not token or "." not in token:
        return None
    try:
        body, sig = token.split(".", 1)
        payload = _unb64(body)
        expected = hmac.new(_secret(), payload, hashlib.sha256).digest()
        if not hmac.compare_digest(_unb64(sig), expected):
            return None
        data = json.loads(payload)
        if int(data.get("exp", 0)) < time.time():
            return None
        return data.get("u")
    except Exception:  # noqa: BLE001
        return None


# ── user operations ─────────────────────────────────────────────────────────

def normalize_email(email: str) -> str:
    return (email or "").strip().lower()


def create_user(session, email: str, password: str, display_name: str = "",
                role: str = "analyst") -> Tuple[Optional[RegUser], Optional[str]]:
    """Create a user. Returns (user, error) — never raises on user error."""
    email = normalize_email(email)
    if "@" not in email or "." not in email.split("@")[-1]:
        return None, "Enter a valid email address."
    problem = password_problem(password)
    if problem:
        return None, problem
    if find_user(session, email) is not None:
        return None, "An account with that email already exists."
    user = RegUser(
        user_id=f"u-{secrets.token_hex(6)}", email=email,
        display_name=(display_name or email.split("@")[0]).strip()[:120],
        password_hash=hash_password(password), role=role, active=True)
    session.add(user)
    session.commit()
    return user, None


def find_user(session, email: str) -> Optional[RegUser]:
    from sqlalchemy import select
    return session.scalars(
        select(RegUser).where(RegUser.email == normalize_email(email))).first()


def authenticate(session, email: str, password: str) -> Tuple[Optional[RegUser], Optional[str]]:
    user = find_user(session, email)
    # Same message either way: never reveal whether an email is registered.
    if user is None or not user.active or not verify_password(password, user.password_hash):
        return None, "Email or password is incorrect."
    user.last_login = datetime.now(timezone.utc)
    session.commit()
    return user, None


def user_public(user: RegUser) -> dict:
    return {"user_id": user.user_id, "email": user.email,
            "display_name": user.display_name, "role": user.role}
