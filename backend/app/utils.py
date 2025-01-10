from passlib.context import CryptContext
import random
import string

# Initialize Passlib for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def generate_otp(length=6) -> str:
    return ''.join(random.choices(string.digits, k=length))
