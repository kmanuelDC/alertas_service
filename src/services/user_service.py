
from repository.user_repo import UserRepository
from services.encripter_service import encrypt_data
from flask import jsonify

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def register_user(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Faltan campos"})

        self.user_repository.create_user(username, password)
        return {"message": "Usuario creado exitosamente"}

    def authenticate_user(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise ValueError("Faltan campos requeridos.")

        encrypted_password = encrypt_data(password)
        user = self.user_repository.authenticate_user(username, encrypted_password)

        if not user:
            raise ValueError("Credenciales inválidas.")
        
        return {
            "message": "Inicio de sesión exitoso.",
            "user_id": user['id'],
            "username": user['username']
        } 
