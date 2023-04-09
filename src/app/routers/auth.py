from fastapi import APIRouter, status, Body, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
import os

from helpers.auth import create_access_token, verify_password
from database.schemas import StudentSchema, StudentBase, Token
from database.queries import Student
from database.db import get_db
from middleware.auth import is_autheticated

from exceptions.user import user_not_found_exception, incorrect_password_exception, user_already_exists_exception

router = APIRouter(
    prefix="/api/v1/auth",
)

@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
def login(id: str = Body(...), password: str = Body(...), db: Session = Depends(get_db)):
    user = Student.get_student_by_id(id, db)
    if not user:
        raise user_not_found_exception
    if not verify_password(password, user.password):
        raise incorrect_password_exception
    access_token_expires = timedelta(minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={
            "id": user.id,
            "email" : user.email
        },
        expires_delta=access_token_expires
    )
    return Token(access_token=f"Bearer {access_token}")

