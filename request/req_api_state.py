# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import json
import traceback
import re
import requests
import settings.settings_api as settings
import random


def print_responseNoIndent(response,status_code, request_type):
    print('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    print('STATUS CODE: '+status_code)
    if response != 'NO':
        print('CONTENT: '+str(response.content))

def insert_state_machine_process(state_process_machine):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_STATE
    state_machine_process_req = json.dumps(state_process_machine.__dict__, indent=4)
    response = None
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.post(uri, data=state_machine_process_req,headers=headers)
    except Exception as e:
        print('[STACKTRACE] POST::REQ_API_SUBITO_MESSAGE: ' + str(e))
        pass

    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent(response, str(response.status_code), 'POST')
    return response    

def update_state_machine_process(state_machine_process):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_STATE + str(state_machine_process.id_state_machine)
    state_machine_process_req = json.dumps(state_machine_process.__dict__, indent=4)
    response = None
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.put(uri, data=state_machine_process_req,headers=headers)
    except Exception as e:
        print('[STACKTRACE] PUT::REQ_API_SUBITO_MESSAGE: ' + str(e))
        pass

    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent(response, str(response.status_code), 'PUT')
    return response   

def get_id_of_last_state_machine_process():
    uri = settings.BASE_URI + settings.PORT + settings.LAST_STATE
    response = None
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    reponseDecodedUtf8 = response.content.decode('utf-8')
    temp = re.findall(r'\d+', reponseDecodedUtf8)
    response_cleaned = list(map(int, temp))

    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent('NO', str(response.status_code),'GET')
    return response_cleaned[0]

def get_state_machine_process_by_id(id):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_STATE + str(id)
    response = None
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent('NO', str(response.status_code),'GET')
    return response.content

