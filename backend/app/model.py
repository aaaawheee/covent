from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from database import Base

class UserType(PyEnum):
    SPONSOR = "Sponsor"
    EVENT_ORGANISER = "Event Organiser"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)  # For email verification
    otp = Column(String, nullable=True)          # For OTP handling
