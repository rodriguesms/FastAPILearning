from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#path operation decorator
#path operation function

@app.get('/')
def Home():
    return {'data': 'blog list'}

@app.get('/blog')
def Index(limit = 10, published:bool = True, sort: Optional[str] = None ): 
    # = sets default state | optional default state
    
    if published:
        return {'data' : f'{limit} published blogs from the db'}
    else:
        return {'data' : f'{limit} blogs from the db'}

@app.get('/about')
def About():
    return {'data': 'about page'}


@app.get('/blog/unpublished')
def Unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def Show(id:int):
    # fetch blog with id = id
    return {'data' : id}


@app.get('/blog/{id}/comments')
def Comments(id):
    #fetch comments of blog with id = id
    return {'data': {'1', '2'}} 

@app.post('/blog')
def Create_Blog():
    return {'data' : "Blog is created"}
