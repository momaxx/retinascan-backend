from fastapi import FastAPI
# Rest of your code...

 app = FastAPI()

 @app.get("/")
 def read_root():
     return {"Hello": "World"}
