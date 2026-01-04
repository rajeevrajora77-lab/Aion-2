from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime
