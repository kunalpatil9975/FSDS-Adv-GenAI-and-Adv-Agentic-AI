from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    # name: str 
    name : str = "Ajay"
    age : Optional[int] = None
    email : EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5)


new_student = {'age' : '40', 'email' : 'abc@gmail.com' ,'cgpa': 1 }

student = Student(**new_student)
#student is a pydentic object. We can convert it to a dictionary or json if needed.
print(student)
print(type(student))

student_dict = dict(student)
print(type(student_dict))
print(student_dict)


student_json = student.model_dump_json()
print(student_json)

print(type(student_json))

# JSON is fundamentally text format (string representation)
# Even though it looks like a dictionary, it is actually a serialized string representation of the data. To convert it back to a dictionary, we can use json.loads() method from the json module in Python.


