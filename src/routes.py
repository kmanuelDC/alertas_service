from flask import Blueprint, jsonify
from controllers.condiciones_controller import CondicionesController
from controllers.fleets_controller import FleetsController
from controllers.user_controller import UserController


routes = Blueprint('routes', __name__)

controller = {
     "conditions": CondicionesController(),
     "fleets": FleetsController(),
     "user" : UserController()
 }


# Alertas
routes.add_url_rule('/v1/get/all/conditions', view_func=controller['conditions'].get_conditions, methods=['GET'])
routes.add_url_rule('/v1/get/levels', view_func=controller['conditions'].get_levels, methods=['GET'])
routes.add_url_rule('/v1/get/operators', view_func=controller['conditions'].get_operators, methods=['GET'])

routes.add_url_rule('/v1/post/rule/condition', view_func=controller['conditions'].insert_condition, methods=['POST'])
routes.add_url_rule('/v1/delete/condition', view_func=controller['conditions'].delete_condition, methods=['PUT'])


routes.add_url_rule('/v1/get/condition/by/id', view_func=controller['conditions'].get_condition_rule_detail_by_id, methods=['GET'])

# FLOTAS
routes.add_url_rule('/v1/get/fleets', view_func=controller['fleets'].get_fleets, methods=['GET'])

#PARAMETERS
routes.add_url_rule('/v1/get/all/parameters', view_func=controller['conditions'].get_all_parameters, methods=['GET'])

#USERS
routes.add_url_rule('/v1/create/user', view_func=controller['user'].create_user, methods=['POST'])
routes.add_url_rule('/v1/init/session', view_func=controller['user'].init_session, methods=['POST'])


