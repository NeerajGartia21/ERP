from pydantic import BaseModel

class Token(BaseModel):
    access_token: str

# Base class is schema for request body
class StudentBase(BaseModel):
    email: str
    full_name: str
    password: str

# Schema class is schema for response body and db object
class StudentSchema(StudentBase):
    id: str
    department_id = str
    # allows conversion between Pydantic and ORMs
    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    id: str