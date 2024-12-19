from database.connection import get_connection_alertasDB

class BaseRepository:
    
    @classmethod
    def get_data_db(self,query):
        # return True
        try:
            conection = get_connection_alertasDB()
            result = []
            # print(conection)
            with conection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                # print(result)
                cursor.close()
            return result

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def insert_data_db(cls, insert_query):
        try:
            connection = get_connection_alertasDB()
            with connection.cursor() as cursor:
                cursor.execute(insert_query)
            connection.commit()
        except Exception as ex:
            connection.rollback()
            raise Exception(ex)