from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

# test main file | only for practice
# to run the aplication, create and start a python enviroment folder
# install the depedencies on requirements.txt
# remember to update the pip


app = FastAPI()

# path operation decorator
# path operation function

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


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def Create_Blog(blog: Blog):
    return {'data' : f"Blog was created with title as {blog.title}."}


#if __name__ == "__main__":
#   uvicorn.run(app, host="127.0.0.1", port=9000)
