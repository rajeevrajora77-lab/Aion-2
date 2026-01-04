from fastapi import APIRouter
from pydantic import EmailStr
from uuid import uuid4
from app.auth.jwt import create_access_token

router = APIRouter()

@router.post("/login")
def login(email: EmailStr):
    """
    v1: Trust-based email login
    v2: Plug OTP here
    """
    user_id = str(uuid4())
    token = create_access_token(user_id)

    return {
        "user_id": user_id,
        "access_token": token,
        "token_type": "bearer"
    }
