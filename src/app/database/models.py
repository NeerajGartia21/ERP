from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Text

from .db import Base

class Student(Base):
    __tablename__= 'student'
    id = Column(String(20), primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)
    full_name = Column(String(20))
    password = Column(String(20))
    department_id = Column(String(20), ForeignKey("department.id"))
    address = Column(Text)
    faculty_advisor = Column(String(20), ForeignKey("faculty.id"))

class Faculty(Base):
    __tablename__= 'faculty'
    id = Column(String(20), primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)
    full_name = Column(String(20))
    password = Column(String(20))
    department_id = Column(String(20), ForeignKey("department.id"))

class Department(Base):
    __tablename__= 'department'
    id = Column(String(20), primary_key=True, index=True)
    name = Column(String(20))

class Course(Base):
    __tablename__= 'course'
    id = Column(String(20), primary_key=True, index=True)
    name = Column(String(20))
    department_id = Column(String(20), ForeignKey("department.id"))
    credits = Column(Integer)
    faculty_id = Column(String(20), ForeignKey("faculty.id"))

class CourseEnrolled(Base):
    __tablename__= 'course_enrolled'
    course_id = Column(String(20), ForeignKey("course.id"), primary_key=True, index=True)
    student_id = Column(String(20), ForeignKey("student.id"), primary_key=True, index=True)
    grade = Column(Integer)
    status = enumerate("ongoing, completed")
    semester = Column(Integer)
