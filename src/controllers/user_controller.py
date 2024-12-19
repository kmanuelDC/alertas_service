from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_service = UserService()


class UserController():

    def init_sesion(self, request):
        user_service.init_sesion(request)
        return True

    def create_user(self):
        data = request.get_json()
        # print(data)
        # print(prin)
        resp = user_service.register_user(data)
        return resp