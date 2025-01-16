from base.base_repository import BaseRepository
from database.queries.query_user import query
from services.encripter_service import encrypt_data,verify_password


class UserRepository:
    def __init__(self):
        self.base = BaseRepository()

    def get_user_by_username(self, username):
        try:
            query_str = query['get_user_by_username'](username)
            result = self.base.get_data_db(query_str)
            #print('query_str', result)
            return result[0] if result else None
        except Exception as ex:
            raise RuntimeError(f"Error al loguear: {str(ex)}")

    def authenticate_user(self, username, password):
        try:
            user = self.get_user_by_username(username)
            if not user:
                return None
            
            stored_password = user[2]
            if verify_password(password, stored_password):
             print("Contraseña correcta")
             return {
                    "id": user[0],
                    "username": user[1]
                }
             
            return None  
        except Exception as ex:
            raise RuntimeError(f"Error al loguear: {str(ex)}")
        
    def user_exists(self, username):
        query_str = f"""
            SELECT COUNT(1)
            FROM tp_users
            WHERE user_name = '{username}' AND time_delete IS NULL;
        """
        result = self.base.get_data_db(query_str) 
        return result[0][0] > 0 

    def create_user(self, name, password):
        if self.user_exists(name):
            raise ValueError(f"El usuario '{name}' ya existe.") 
        try:
            encrypted_password = encrypt_data(password)
            query_str = query['create_user'](name, encrypted_password)
            self.base.insert_data_db(query_str)
            return {"message": "Usuario creado exitosamente"}
        except Exception as ex:
            raise RuntimeError(f"Error al crear el usuario: {str(ex)}")
