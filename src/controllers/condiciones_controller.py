from repository.conditiones_repo import ConditionsRepository
from flask import jsonify,request


repo = {
    "conditions": ConditionsRepository()
 }


class CondicionesController():
    def get_conditions(self):
        resp = repo['conditions'].get_conditions()
        return jsonify({"data": resp}), 200
    
    def insert_condition(self):
        try:
            req = request.json

            # Validar si 'newrule' existe en el JSON recibido
            if 'newrule' not in req:
                return jsonify({"error": "newrule no está presente en la solicitud"}), 400
            newrule = req['newrule']
            resp = repo['conditions'].insert_condition(newrule)
            
            return jsonify({"data": resp}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def delete_condition(self):
        req = request.args
        resp = repo['conditions'].delete_condition(req)
        return jsonify({"data": 'true' if resp is True else 'false'}), 200

    def get_levels(self):
        resp = repo['conditions'].get_levels()
        return jsonify({"data": resp}), 200

    def get_operators(self):
        resp = repo['conditions'].get_operators()
        return jsonify({"data": resp}), 200

    def get_all_parameters(self):
        resp = repo['conditions'].get_all_parameters()
        return jsonify({"data": resp}), 200

    def get_condition_rule_detail_by_id(self):

        try: 
            req = request.args
            resp = repo['conditions'].get_condition_rule_detail_by_id(req['id'])
            return jsonify({"data": resp}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500