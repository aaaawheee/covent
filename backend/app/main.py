from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import schemas, auth_service, database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return auth_service.register_user(user, db)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return auth_service.authenticate_user(user.email, user.password, db)

@app.post("/forgot-password")
def forgot_password(data: schemas.PasswordResetRequest, db: Session = Depends(get_db)):
    return auth_service.send_otp(data.email, db)

@app.post("/reset-password")
def reset_password(data: schemas.PasswordReset, db: Session = Depends(get_db)):
    return auth_service.reset_password(data.email, data.otp, data.new_password, db)
