from base.base_repository import BaseRepository
from database.queries.query_db import query
from services.condition_service import generar_id
from flask import jsonify,request
from itertools import groupby
from operator import itemgetter

base = BaseRepository()

class ConditionsRepository():
    
    @classmethod
    def get_conditions(self):
        result = base.get_data_db(query['get_conditions']())
        return result
    
    def insert_condition(self,obj):        
        try: 

            # print(obj['logica'])
            id_cond = generar_id()
            body_rule_insert = []
            body_rule_detail_insert = []
            
            for rule in obj['logica']['rules']:
                id_cond_rule = generar_id()
                op_rule = obj['logica']['operator'] if obj['logica']['operator'] else None
                row_rule = f"('{id_cond_rule}','{id_cond}',{op_rule if op_rule is not None else 'null'})"
                body_rule_insert.append(row_rule)

                for conditional in rule['conditionals']:
                    row_rule_detail = f"({conditional['value']},'{id_cond_rule}', {conditional['id_parameter']},{conditional['symbol']}, { (1 if op_rule == 2 else 2) if op_rule is not None else 'null'})"
                    body_rule_detail_insert.append(row_rule_detail)
            
            base.insert_data_db(query['insert_new_condition'](id_cond,obj))
            base.insert_data_db(query['head_insert_new_rule_condition'](", \n ".join(body_rule_insert)))
            base.insert_data_db(query['head_insert_new_rule_condition_detail'](", \n ".join(body_rule_detail_insert)))
            
            print('NUEVA CONDICION INGRESADA')
            
            return True
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def delete_condition(self,req):
        result = base.insert_data_db(query['delete_condition'](req['id']));
        return True

    def get_levels(self):
        result = base.get_data_db(query['get_levels']())
        return result

    def get_operators(self):
        result = base.get_data_db(query['get_operators']())
        return result

    def get_all_parameters(self):
        result = base.get_data_db(query['get_all_parameters']())
        return result

    def get_condition_rule_detail_by_id(self,id):
        # print(obj)
        result = base.get_data_db(query['get_condition_rule_detail_by_id'](id))
        # print(result)
        grupos = {}
        for x in result:
                clave = (x[7])
                grupos.setdefault(clave, []).append(x)
                
        obj = {
            'name': result[0][0],
            'fleet': result[0][1],
            'level': result[0][2],
            'color': result[0][3],
            'notify': result[0][5],
            'operatorRule': result[0][4],
            'emails': result[0][6],
            'rules': grupos
            }

        return obj

    def get_last_times_equipments(self):
        result = base.get_data_db(query['get_last_times_equipments']())
        return result
    
    def get_configurations_conditions(self):
        data = base.get_data_db(query['get_config_conditions']('true'))
        # Agrupar por 'condition_id'
        grouped_data = []
        data.sort(key=itemgetter(0))
        for condition_id, items in groupby(data, key=itemgetter(0)):
            items = list(items)
            rules = []
            for codition_rule_id, rules_group in groupby(sorted(items, key=itemgetter(2)), key=itemgetter(2)):
                rules.append([{
                    'param_id': rule[8],
                    'operator': rule[7],
                    'limit': rule[10],
                    'relation': rule[9]
                } for rule in rules_group])
            # Agrupar los 'rules' por la columna 2 (codition_rule_id)
            # Construir el objeto agrupado
            grouped_data.append({
                'condition_id': condition_id,
                'condition_name': items[0][1],  # Columna 1: condition_type_id
                'condition_fleets': items[0][2],  # 
                'condition_has_notification': items[0][3],  # Si tienes este valor en tus datos
                'condition_from_emails': items[0][4],  # 
                'condition_params': [item[8] for item in items],  # Columna 3: params
                'condition_critical': items[0][13], # Si tienes este valor en tus datos
                'condition_sound': True,  # 
                'level_name': items[0][12],  # 
                'rules': rules  # Agregar las reglas agrupadas
            })
            

        # print(f"""{grouped_data}\n""")
    
        return grouped_data

    def get_last_events_no_closed(self):
        result = base.get_data_db(query['get_last_events_no_closed']())
        return result

    def get_equipments(self):
        result = base.get_data_db(query['get_equipments']())
        return result
        
    def generate_alerts(self,config_list, data_all, last_events_no_closed):
    #     # eventsProcessed = []
        print(data_all)
        data_all.sort(key=lambda x: x['id_equipment']) 
        grouped_data = groupby(data_all,key=lambda x:x['id_equipment'])
        print(grouped_data)
        for configuration in config_list:
            print('')
            
            
            # print(grouped_data)
            # events_no_closed = next(evn['data'] for evn in last_events_no_closed if int(evn['condition_id']) == int(configuration['condition_id'])),None
            # print(events_no_closed)
            # events_not_closed = next(evn['data'] for evn in last_events_no_closed if int(evn['condition_id']) == int(configuration['condition_id'])),None


    #         events_not_closed = next((evn.data for evn in last_events_no_closed if int(evn['condition_id']) == int(configuration['condition_id'])), None)
    #         print(events_not_closed)
    # Your code here

        # print('oliiiiz')
