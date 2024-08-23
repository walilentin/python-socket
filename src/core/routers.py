import json

from src.core.http_router import router


@router.get('/')
def index():
    with open('src/templates/index.html') as template:
        return template.read()

@router.post('/submit-form')
def submit_form(body):
    return body

@router.get('/me')
def me():
    return {'hello':'world'}

@router.get('/blog')
def blog():
    return "<h1>Blog</h1>"