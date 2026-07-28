from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):
    
    name : str = "Ajay"
    age : Optional[int] = None
    email : EmailStr
    

new_student = {'age' : '40', 'email':'abc@gmail.com' } #pip install email-validator

student = Student(**new_student)

print(student)



