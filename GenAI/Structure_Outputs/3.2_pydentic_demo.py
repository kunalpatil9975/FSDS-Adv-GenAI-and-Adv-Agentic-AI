from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):

    name : str = "Ajay"
    age : Optional[int] = None



#new_student = {}
#new_student = {'age' : 40}
new_student = {} #(type coercion)this will work because pydantic will try to convert the string to int if possible, otherwise it will raise a validation error    
#type coercion means Pydantic tries to automatically convert input data into the expected type

student = Student(**new_student)


print(student)
print(type(student))
