from pydantic import BaseModel,EmailStr,Field   #In Pydantic, Field is a helper function used to add metadata, validation rules, and constraints to model attributes inside a class that inherits from BaseModel. It allows you to specify additional information about the fields in your model, such as default values, validation criteria, and descriptions. By using Field, you can enhance the functionality and validation of your Pydantic models.
from typing import Optional

class Student(BaseModel):
    # name: str 
    name : str = "Ajay"
    age : Optional[int] = None
    email : EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description="CGPA must be between 0 and 10")


#new_student = {'age' : '40', 'email' : 'abc@gmail.com' ,'cgpa': 9 }
new_student = {'age' : '40', 'email' : 'abc@gmail.com' , 'cgpa': 9} #this will raise a validation error because cgpa is greater than 10}


student = Student(**new_student)


print(student)


