# import fastapi
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "Year 12"
    },
    2: {
        "name": "Jane",
        "age": 16,
        "year": "Year 11"
    }
}

class Student( BaseModel):
    name: str
    age:int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# option 1
@app.delete("/del-student")
def delete_student(id: int = None):
    if id not in students:
        return {"Error": "Student does not exist"}
    else:
        del students[id]
        return {"Message": "Student deleted successfully"}

# option 2
@app.delete("/delete-student/{id}}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    else:
        del students[student_id]
        return {"Message": "Student deleted successfully"}


@app.put("/update-student/{student_id}")
def uodate_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    else:
        if student.name != None:
            students[student_id].name = student.name
        if student.age != None:
            students[student_id].age = student.age
        if student.year != None:
            students[student_id].year = student.year
    
    return students[student_id]


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    else:
        students[student_id] = student
        return students[student_id]


# @app.get("/get-student?name={name}")
@app.get("/get-student")
# def get_student_by_name(name: str):
# def get_student_by_name(name: str = None): # default value to None so that it becomes not required
# def get_student_by_name(name: Optional[str] = None): # makes name paramater Optional
# def get_student_by_name(name: str = Optional[str], test = int): # would cause error as optional parameter can not come before required parameter
def get_student_by_name(*, name: str = None, test = int): # asterics makes rest of the parameters optional 
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not Found"}

# gets assertion error because Path cannot be None or any other default value
# @app.get("/get-student/{student_id}")
# def get_student2(student_id: int = Path(None, description="The ID of the student you want to view")):
#     return students[student_id]

@app.get("/get-student/{student_id}")
def get_student2(student_id: int= Path( ..., gt=0, lt=3, description="The ID of the student you want to view") ):
    return students[student_id]


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/")
def index():
    return {"message": "Hello World"}