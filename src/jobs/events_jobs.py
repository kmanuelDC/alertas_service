from repository.conditiones_repo import ConditionsRepository

import requests
from datetime import datetime
from services import read_write
from decouple import config
from flask import jsonify,request



def alerts_pre_config():
    equipments_times = ConditionsRepository().get_last_times_equipments()
    now = datetime.now()

    last_time= None

    if(equipments_times):
        for equip in equipments_times:
            if datetime.strptime(equip[0], "%Y-%m-%d %H:%M:%S") > now:
                last_time = equip[0]
            else:
                last_time = now
                

    print(last_time)

def generate_alerts():
    # print('alerta generada')
    try:
        # print('')
        last_execution = read_write.read_json_file('src/config.db.json')
        config_list = ConditionsRepository().get_configurations_conditions()
        parameters = list({item for sublist in config_list for item in sublist['condition_params']})
        last_events_no_closed = ConditionsRepository().get_last_events_no_closed()
        equipments = ConditionsRepository().get_equipments()
        print(equipments)
        url = config('URL_API_GET_DATA')
        # print(f"""{url}?{'fecha='}{last_execution['last_update']}&{'parameters='}&{'parameters='}{}""")
        if(config):
         response = requests.get(f"""{url}?{'fecha='}{last_execution['last_update']}&{'parameters='}{"1,2,3"}""")
        # response = requests.get(f"""{url}?{'fecha='}{last_execution['last_update']}&{'parameters='}&{'parameters='}{",".join(map(str, parameters))}""")
         if response.status_code == 200:
          data_all = response.json()
          if (data_all):
                # print(last_events_no_closed)
                ConditionsRepository().generate_alerts(config_list, data_all['data'], last_events_no_closed)
                # print(data_all['data'])
        else:
            print(f"Error al hacer la solicitud: {response.status_code}")
        
        # print(last_execution.get('last_update'))
    except Exception as e:
            return jsonify({"error": str(e)}), 500
        