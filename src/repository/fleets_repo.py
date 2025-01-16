from base.base_repository import BaseRepository
from database.queries.query_db import query

base = BaseRepository()

class FleetsRepository():
    
    @classmethod
    def get_fleets(self):
        result = base.get_data_db(query['get_fleets']())
        return result
