# import fastapi
from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "Year 12"
    },
    2: {
        "name": "Jane",
        "age": 16,
        "class": "Year 11"
    }
}

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