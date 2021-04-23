from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def HomePage():
    return {'data': {'name': 'Miguel'}}

@app.get('/about')
def AboutPage():
    return {'data': 'about page'}