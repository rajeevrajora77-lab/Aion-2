from fastapi import Depends, HTTPException, Header
from jose import JWTError
from app.auth.jwt import decode_token

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        token = authorization.replace("Bearer ", "")
        payload = decode_token(token)
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
