from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# Jinja2 Templates for HTML 
from fastapi.templating import Jinja2Templates

# Mount static directory


# Configure Templates
templates = Jinja2Templates(directory='templates')

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount(
    "/static", # URL prefix
    StaticFiles(directory="static"), # Actual folder on your computer
    name="static") # Name used by url_for()




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

# @app.get('/', response_class=HTMLResponse, include_in_schema=False)
# @app.get('/posts', response_class=HTMLResponse, include_in_schema=False)



@app.get('/', include_in_schema=False)
@app.get('/posts', include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, 'home.html')


@app.get('/api/posts', response_class = HTMLResponse)
def get_posts():
    return posts