
def get_conditions():
    query = f"""select tpc.id,tpc.name,f.fleet_name,lvl.name,critical,sound,notify,from_emails from tp_condition tpc
              left join public.fleets f on tpc.fleet = f.fleet
              left join public.ts_level_alarm lvl on tpc.level_id = lvl.id
              where time_delete is null;"""
    return query

def delete_condition(id):
    query = f"""update tp_condition set time_delete = now() where id = '{id}';"""
    return query

def get_levels():
    query = "select * from ts_level_alarm;"
    return query

def get_operators():
    query = "select * from ts_rules_relations;"
    return query


#FLEETS

def get_fleets():
    query = "select * from fleets;"
    return query

#PARAMETROS
def get_all_parameters():
    query = "select * from tp_parametros_monitoreo;"
    return query

def get_last_id_condition():
    query = "select id from tp_condition order by id desc;"
    return query

def get_last_id_condition_rule():
    query = "select id from tp_condition_rules order by id desc;"
    return query

##INSERTS
def insert_new_condition(id,row):
    emails = ', '.join([f"'{email}'" for email in row['emails']])
    query = f"""INSERT INTO public.tp_condition (id, name, level_id, fleet, notify, from_emails, time_create, time_update, time_delete, critical, sound, period_min_for_notification) VALUES
                ('{id}','{row['name']}', {row['level_id']}, {row['fleet_id']}, {str(row['notify']).lower()},{f'ARRAY[{emails}]' if emails else 'null'},now(),null,null,{row['critical']} , {row['sound']}, 30);"""
    # print(quer.y)
    return query

def head_insert_new_rule_condition(body):
    query = f"""INSERT INTO public.tp_condition_rules (id, condition_id, operator)
                VALUES
                {body};"""
    return query

def head_insert_new_rule_condition_detail(body):
    query = f"""INSERT INTO public.tp_condition_rules_details ( value,condition_rule_id_fk, parameter_id, relation, operator ) 
                VALUES
                {body};"""
    return query

def get_condition_rule_detail_by_id(id):
    query=f"""select tpc.name,fleet_name,tla.name,tla.color,tcr.operator,tpc.notify,tpc.from_emails,
                tcrd.condition_rule_id_fk,tpm.nombre_parametro,rel.simbol,tcrd.value,tcrd.relation from tp_condition tpc
                left join fleets fs on fs.fleet = tpc.fleet
                left join ts_level_alarm tla on tpc.level_id = tla.id
                left join tp_condition_rules tcr on tpc.id = tcr.condition_id
                left join tp_condition_rules_details tcrd on tcr.id = tcrd.condition_rule_id_fk
                left join tp_parametros_monitoreo tpm on tcrd.parameter_id = tpm.id_parametro
                left join ts_rules_relations rel on rel.id = tcrd.operator::int
                where tpc.id = '{id}';
                """
    return query

### CRONS
def get_last_times_equipments():
    query="select start_date,equipment_name from tp_alarms_notify where fleet_id in (select fleet from tp_condition group by fleet);"
    return query

def get_config_conditions(isCritical):
    query = f"""select * from config_conditions c where critical = {isCritical} order by c.codition_rule_logical_operator,condition_id;"""
    return query

def get_last_events_no_closed():
    query=f"""select al.id,equipment_id,start_date,condition_id
            from tp_alarms_notify al
            left join tp_condition c on al.condition_id = c.id::int
            where al.end_date  is null;"""
    return query

def get_equipments():
    query = f"""select * from tp_equipos where tiem_elimin is null;"""
    return query


query = {
    "get_conditions": get_conditions,
    
    "delete_condition": delete_condition,
    "get_levels": get_levels,
    "get_operators": get_operators,
    #PARAMETROS
    "get_all_parameters": get_all_parameters,

    #FLEETS
    "get_fleets": get_fleets,
    "insert_new_condition": insert_new_condition,
    "head_insert_new_rule_condition": head_insert_new_rule_condition,
    "head_insert_new_rule_condition_detail": head_insert_new_rule_condition_detail,
    "get_condition_rule_detail_by_id": get_condition_rule_detail_by_id,
    "get_last_times_equipments": get_last_times_equipments,

    ##CRONS
    "get_config_conditions": get_config_conditions,
    "get_last_events_no_closed": get_last_events_no_closed,
    "get_equipments": get_equipments 
    }