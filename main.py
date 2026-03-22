from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Zaki! FastAPI is running."}

@app.get("/test")
def read_test():
    return {"message": "Test endpoint is working correctly."}

@app.get("/greetings")
def read_greetings():
    return {"message": "Hello! This is the new greetings endpoint."}
@app.get("/nullclaw")
def read_nullclaw():
    return {"message": "Welcome to the NullClaw workspace, Zaki!"}

@app.get("/status")
def read_status():
    return {"status": "operational", "user": "Zaki"}

@app.get("/info")
def read_info():
    return {"info": "This is a new endpoint added by Joi."}
@app.get("/joi")
def read_joi():
    return {"message": "Hello Zaki, Joi is here to help!"}

