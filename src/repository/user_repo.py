from base.base_repository import BaseRepository
from database.queries.query_user import query
from services.encripter_service import encrypt_data
from flask import jsonify


base = BaseRepository()

class UserRepository:
    
    @classmethod
    def get_user(self):
        result = base.get_data_db(query['get_user']())
        return result

    @classmethod
    def create_user(self, name, password):
        try:
            print(name, password)
            # password = encrypt_data(password)
            print(password)
            # result = base.insert_data_db(query['create_user'](name, password))
            return jsonify({"data": "OK"})
        except Exception as ex:
            raise ex