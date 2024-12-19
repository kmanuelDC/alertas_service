
from repository.user_repo import UserRepository
from flask import jsonify

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def register_user(self, data):
        """Registra un nuevo usuario."""
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Faltan campos"})
        
        return self.user_repository.create_user(username, password)

    def init_sesion(request):
        return 'hastaAqui'