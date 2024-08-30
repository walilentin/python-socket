from src.core.http_router import Router
from src.users.router import user_router

main_router = Router()

main_router.add_router(user_router)


@main_router.get('/')
def index():
    with open('src/templates/index.html') as template:
        return template.read()