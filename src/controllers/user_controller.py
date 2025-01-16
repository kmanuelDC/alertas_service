from flask import request, jsonify
from services.user_service import UserService

user_service = UserService()


class UserController():

    def create_user(self):
        try:
            data = request.get_json()
            response = user_service.register_user(data)
            return jsonify(response), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as ex:
            return jsonify({"error": "Error interno del servidor"}), 500

    def init_session(self):
        try:
            data = request.get_json()
            response = user_service.authenticate_user(data)
            return jsonify(response), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as ex:
            return jsonify({"error": "Error interno del servidor"}), 500

    