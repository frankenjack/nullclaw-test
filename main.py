from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Zaki! FastAPI is running."}

@app.get("/test")
def read_test():
    return {"message": "Test endpoint is working!"}