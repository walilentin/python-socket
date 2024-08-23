class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, method, path):
        def decorator(func):
            self.routes[(method, path)] = func
            return func

        return decorator

    def get(self, path):
        return self.add_route('GET', path)

    def post(self, path):
        return self.add_route('POST', path)

    def put(self, path):
        return self.add_route('PUT', path)

    def delete(self, path):
        return self.add_route('DELETE', path)

router = Router()