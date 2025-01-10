from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import model, schemas, utils
from database import SessionLocal

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def register_user(user: schemas.UserCreate, db: Session):
    # Check if email exists
    db_user = db.query(model.User).filter(model.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password
    hashed_password = utils.hash_password(user.password)

    # Create user
    new_user = model.User(
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(email: str, password: str, db: Session):
    db_user = db.query(model.User).filter(model.User.email == email).first()
    if not db_user or not utils.verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return db_user

def send_otp(email: str, db: Session):
    user = db.query(model.User).filter(model.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = utils.generate_otp()
    user.otp = otp
    db.commit()

    # Simulate sending OTP
    print(f"OTP for {email}: {otp}")
    return {"message": "OTP sent to email"}

def reset_password(email: str, otp: str, new_password: str, db: Session):
    user = db.query(model.User).filter(model.User.email == email, model.User.otp == otp).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid OTP or email")

    user.hashed_password = utils.hash_password(new_password)
    user.otp = None
    db.commit()
    return {"message": "Password successfully reset"}
