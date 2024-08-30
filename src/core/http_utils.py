import json
import urllib.parse
from src.main import main_router as router


METHODS = ['GET', 'POST', 'PUT', 'DELETE']

def json_response(data):
    headers = 'HTTP/1.1 200 OK\nContent-Type: application/json\n\n'
    return (headers + json.dumps(data)).encode()

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
        return 'HTTP/1.1 405 Method Not Allowed\n\n', 405
    if (method, url) not in router.routes:
        return 'HTTP/1.1 404 Not Found\n\n', 404
    return 'HTTP/1.1 200 OK\n\n', 200

def generate_response(request):
    method, url = parse_request(request)
    headers, status_code = generate_headers(method, url)

    handler = router.routes.get((method, url))

    if handler:
        if method == 'POST':
            body = parse_body(request)
            response_body = handler(body)
        else:
            response_body = handler()

        if isinstance(response_body, dict):
            return json_response(response_body)
        else:
            return (headers + response_body).encode()
    else:
        return ('HTTP/1.1 404 Not Found\n\n<h1>404</h1><p>Not found</p>').encode()