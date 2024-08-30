from src.core.http_router import Router

user_router = Router()

user_1 = {'name': 'Valentin', 'age': '21', 'sex': 'male'}
user_2 = {'name': 'Bogdan', 'age': '21', 'sex': 'transformer'}

@user_router.get('/me')
def me(user_name =  user_1['name']):
    return user_name