from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


posts: list[dict] = [
    {
        "id":1,
        "author": "Sagar Tiwari",
        "title": "FASTAPI is awesome",
        "content": "This framework is really easy to use and super fast",
        "date_posted": "November 15, 2026",
    },

    {
        "id":2,
        "author":"ABC",
        "title":"Python is Great for Web Development",
        "content":"Python is greate language for web development",
        "date_posted":"January 1, 2026"
    },

]





"""
include_in_schema = False, will hide the api routes.
"""
@app.get('/', response_class=HTMLResponse, include_in_schema=False)
@app.get('/posts', response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get('/api/posts')
def get_posts():
    return posts