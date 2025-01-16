from cryptography.fernet import Fernet
from decouple import config
from bcrypt import checkpw

# Clave secreta para cifrar/descifrar
SECRET_KEY = config('SECRET_KEY', default=Fernet.generate_key().decode())
cipher = Fernet(SECRET_KEY.encode())

def encrypt_data(data: str) -> str:
    #print(data)
    """Cifra datos sensibles."""
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    """Descifra datos cifrados."""
    return cipher.decrypt(data.encode()).decode()

def verify_password(input_password, stored_password):
    try:
        input_decrypted = cipher.decrypt(input_password.encode()).decode()
        stored_decrypted = cipher.decrypt(stored_password.encode()).decode()
        return input_decrypted == stored_decrypted
    except Exception as e:

        print(f"Error al verificar la contraseña: {e}")
        return False
