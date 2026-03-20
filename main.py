from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Zaki! FastAPI is running."}

@app.get("/test")
def read_test():

@app.get("/greetings")
def read_greetings():
    return {"message": "Hello! This is the new greetings endpoint."}
@app.get("/nullclaw")
def read_nullclaw():
    return {"message": "Welcome to the NullClaw workspace, Zaki!"}
