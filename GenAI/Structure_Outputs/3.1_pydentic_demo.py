from pydantic import BaseModel


class Student(BaseModel):

    name : str = "vijay"
  

new_student = {}


student = Student(**new_student)


print(student)
print(type(student))
