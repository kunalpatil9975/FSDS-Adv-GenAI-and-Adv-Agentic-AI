from pydantic import BaseModel


class Student(BaseModel):
    # name: str 
    name : str 
  

new_student = {'name': 32}
#new_student = {'name': 32}


student = Student(**new_student) #type hinting for better code completion and error checking in IDEs


print(student)
print(type(student))
