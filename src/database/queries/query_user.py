def create_user(username, password):
    query = f"""INSERT INTO tp_users (user_name, password, time_creation, time_delete)
                VALUES ('{username}', '{password}', now(), null)
                RETURNING id, user_name, password;"""
    return query

def get_user_by_username(username):
    """Crea una consulta para obtener un usuario por sus credenciales."""
    query = f"""
            SELECT id, user_name, password
            FROM tp_users
            WHERE user_name = '{username}' AND time_delete IS NULL;
        """
    return query

query = {
    "create_user": create_user,
    "get_user_by_username": get_user_by_username
}