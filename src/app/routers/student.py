from fastapi import APIRouter, status, Body, Depends
from sqlalchemy.orm import Session
import os

from database.schemas import StudentSchema, CourseBase
from database.queries import Student, CourseEnrolled
from database.db import get_db
from middleware.auth import is_autheticated

from exceptions.user import user_not_found_exception

router = APIRouter(
    prefix="/api/v1/student",
)

@router.get("/profile", status_code=status.HTTP_200_OK, response_model=StudentSchema)
def get_user(student_id: int = Depends(is_autheticated), db: Session = Depends(get_db)):
    student = Student.get_user_by_id(student_id,db)
    if not student:
        raise user_not_found_exception
    return student

@router.get("/performance", status_code=status.HTTP_200_OK, response_model=CourseBase)
def get_user(student_id: int = Depends(is_autheticated), db: Session = Depends(get_db)):
    student = Student.get_user_by_id(student_id,db)
    if not student:
        raise user_not_found_exception
    course_enrolled = CourseEnrolled.get_enrollment_by_student(student_id, db)
    return course_enrolled

