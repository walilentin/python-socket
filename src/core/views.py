def index():
    with open('src/templates/index.html') as template:
        return template.read()


def blog():
    with open('src/templates/blog.html') as template:
        return template.read()


def me():
    with open('src/templates/me.html') as template:
        return template.read()
