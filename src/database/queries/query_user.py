def create_user(name, password):
    query = f"""INSERT INTO tp_users (user_name, password, time_creation, time_delete)
                VALUES ('{name}', '{password}', now(), null)
                RETURNING id, user_name, password;"""
    return query

query = {
    "create_user": create_user
}