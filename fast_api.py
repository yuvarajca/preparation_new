from fastapi import FastAPI
api = FastAPI()

#GET, POST, PUT, DELETE
@api.get('/')
def index():
    return {'message':'Hello World'}

@api.get('/getdata')
def calculation():
    pass
    return "calculations done"