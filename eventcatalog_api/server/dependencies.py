# Dependency injection definitions
from config import settings
from fastapi import Header, HTTPException


def get_token_header(x_token: str = Header(...)):
    if x_token != settings.secret_key:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token
