from src.core.http_router import router


@router.get('/')
def index():
    with open('src/templates/index.html') as template:
        return template.read()

@router.post('/submit-form')
def submit_form():
    return "<h1>Form Submitted</h1>"

@router.get('/me')
def me():
    return "<h1>ME</h1>"

@router.get('/blog')
def blog():
    return "<h1>Blog</h1>"