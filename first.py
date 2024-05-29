from typing import Union

from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    postId: int
    owner: str

posts = dict()
posts[1]=["Hasnain", "second post", "LinkedIn post for 600 Leetcode"]

def addPost(argPost:Post):
    posts[argPost.postId] = [argPost.owner, argPost.title, argPost.content]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/Sibtain")
def read_root():
    return {"Salam": "Sibtain Ahmed here"}

@app.post("/post_here")
def create_post(postData: Post):
    # print(postData)
    addPost(postData)
    return {"Data": "posted successfully"}


@app.get("/getAllPosts")
def read_item():
    return posts


@app.get("/getPost/{id}")
def read_item(id: int, response: Response):
    if id in posts:
        return {"data": posts[id]}
    else:
        response.status_code = 404
        return {"data": None}
