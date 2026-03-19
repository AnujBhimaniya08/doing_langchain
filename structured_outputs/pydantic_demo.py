from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name : str = "Anuj"
    age : Optional[int] = None
    email : EmailStr = "abc" #built in validation for email, these validations only work for the data that you are entering not on the default data setted there
    cgpa: float = Field(gt=0, lt=10)
 # default values can also put inside the Field
new_student = {'age' : "32", 'cgpa' : '5', 'email' : 'yuk'}
student = Student(**new_student)
student_dict = dict(student)
print(student_dict['email'])