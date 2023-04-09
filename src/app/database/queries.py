from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

from . import models, schemas
from helpers.auth import get_password_hash
from exceptions.user import user_already_exists_exception

class Student:

    @staticmethod
    def get_student_by_id(id: int, db: Session):
        return db.query(models.Student).filter(models.Student.id == id).first()

    @staticmethod
    def get_student_by_email(email: str, db: Session):
        return db.query(models.Student).filter(models.Student.email == email).first()

class Course:

    @staticmethod
    def get_courses_by_department(id: int, db: Session):
        return db.query(models.Course).filter(models.Course.department_id == id)

    @staticmethod
    def get_courses_by_faculty(id: int, db: Session):
        return db.query(models.Course).filter(models.Course.faculty_id == id)
    

class CourseEnrolled:
    
    @staticmethod
    def get_enrollment_by_student(id: int, db: Session):
        return db.query(models.CourseEnrolled).filter(models.CourseEnrolled.student_id == id)

    @staticmethod
    def get_enrollment_by_course(id: int, db: Session):
        return db.query(models.Course).filter(models.Course.faculty_id == id)
    
