def index():
    return '''
    <html>
    <body>
        <h1>Welcome to the index page</h1>
        <form action="/submit-form" method="POST">
            <input type="text" name="username" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    '''


def blog():
    with open('src/templates/blog.html') as template:
        return template.read()


def me():
    with open('src/templates/me.html') as template:
        return template.read()

def submit_form():
    return '<h1>Submit your data</h1>'


