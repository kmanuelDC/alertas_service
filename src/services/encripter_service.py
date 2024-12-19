from cryptography.fernet import Fernet
from decouple import config

# Clave secreta para cifrar/descifrar
SECRET_KEY = config('SECRET_KEY', default=Fernet.generate_key().decode())
cipher = Fernet(SECRET_KEY.encode())

def encrypt_data(data: str) -> str:
    print(data)
    """Cifra datos sensibles."""
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    """Descifra datos cifrados."""
    return cipher.decrypt(data.encode()).decode()