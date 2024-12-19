from repository.fleets_repo import FleetsRepository
from flask import jsonify


repo = {
    "fleets": FleetsRepository()
 }


class FleetsController():
    def get_fleets(self):
        # print('llego paq')
        resp = repo['fleets'].get_fleets()
        return jsonify({"data": resp}), 200
    
