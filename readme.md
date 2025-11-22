# how you run fastapi
    * check if you are in correct directory where your main python script (e.g. main.py or server.py or in this case its myapi.py) for project exists (e.g. dir)
    * then run `uvicorn mayapi:app --reload`
    * fastapi by default makes docs for your all available routes at [http://127.0.0.1:8000]/docs
    * another cool thing about that api docs is that we can directly test them from there without having to use any api client such as postman or thunder client or etc
    * another newer version of docs is [http://127.0.0.1:8000]/redoc