from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')


@api.route('/')
class RegisterView(Resource):
    """Получение информации о пользователе"""
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        data = request.get_json(force=True)
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.get_user_by_token(refresh_token=header)

    """Обновление информации о пользователе. На вход подаётся JSON-словарь"""
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def patch(self):
        data = request.get_json(force=True)
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')

        return user_service.update_user(data=data, refresh_token=header)


@api.route('/password/')
class LoginView(Resource):
    """Обновление пароля. На вход подаётся JSON-словарь в формате (старый и новый пароль:
        {
    "password_1": "5123",
    "password_2": "51234"
    }

    """
    def put(self):
        data = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
        return user_service.update_password(data=data, refresh_token=header)
