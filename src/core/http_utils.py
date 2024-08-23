from src.core.views import index, blog, me

URLS = {
    '/': index,
    '/blog': blog,
    '/me': me,
}


def parse_request(request): # parse request take info about method and url like this (GET HTTP/1.1\r\nHost: localhost:7999)
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]

    return (method, url)


def generate_headers(method, url):
    if not method == "GET":
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(status_code, url):
    if status_code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if status_code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return URLS[url]()


def generate_response(request):
    method, url = parse_request(request)
    headers, status_code = generate_headers(method, url)
    body = generate_content(status_code, url)

    return (headers + body).encode()
