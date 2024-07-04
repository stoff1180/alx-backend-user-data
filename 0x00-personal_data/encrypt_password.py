#!/usr/bin/env python3
"""
    encryption password module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """expect one string argument name password and returns
       a salted, hashed password, which is a byte string.
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks password.
    """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
