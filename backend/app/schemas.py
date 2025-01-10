from pydantic import BaseModel, EmailStr
from enum import Enum

class UserType(str, Enum):
    SPONSOR = "Sponsor"
    EVENT_ORGANISER = "Event Organiser"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordReset(BaseModel):
    email: EmailStr
    otp: str
    new_password: str
