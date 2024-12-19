import random
import string

def generar_id(longitud=8):
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(random.choice(caracteres) for _ in range(longitud))
    return id_aleatorio

