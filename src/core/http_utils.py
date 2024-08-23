import urllib.parse
from src.core.routers import index, blog, me, submit_form

URLS = {
    '/': index,
    '/blog': blog,
    '/me': me,
    '/submit-form': submit_form,
}

METHODS = ['GET', 'POST', 'PUT', 'DELETE']


def parse_request(request):  # parse request take info about method and url like this (GET HTTP/1.1\r\nHost: localhost:7999)
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]

    return (method, url)


def parse_body(request):
    try:
        body = request.split("\r\n\r\n", 1)[1]
        return urllib.parse.parse_qs(body)
    except IndexError:
        return {}


def generate_headers(method, url):
    if method not in METHODS:
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(status_code, url, method='GET', body=None):
    if status_code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if status_code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'

    if method == 'POST' and url == '/submit-form':
        return f"<h1>Form submitted successfully!</h1><p>Received data: {body}</p>"

    if url in URLS:
        return URLS[url]()

    return '<h1>404</h1><p>Not found</p>'


def generate_response(request):
    method, url = parse_request(request)
    headers, status_code = generate_headers(method, url)
    body = parse_body(request)
    response_body = generate_content(status_code, url, method, body)
    print(f"Request Method: {method}, URL: {url}")
    print(f"Request Body: {body}")
    return (headers + response_body).encode()