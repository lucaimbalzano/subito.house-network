# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import json
import traceback
import re
import requests
from service.response.res_api_track import get_track_object_from_json
import settings.settings_api as settings
import random





def print_responseNoIndent(response,status_code, request_type):
    print('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    print('STATUS CODE: '+status_code)
    if response != 'NO':
        print('CONTENT: '+str(response.content))

def insert_track_process(track_process):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_TRACK
    track_process_req = json.dumps(track_process.__dict__, indent=4)
    response = None
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.post(uri, data=track_process_req,headers=headers)
    except Exception as e:
        print('[STACKTRACE] POST::REQ_API_SUBITO_MESSAGE: ' + str(e))
        pass
    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent(response, str(response.status_code), 'POST')
    return response    

def update_track_process(track_process):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_TRACK + str(track_process.identifierProcess)
    track_process_req = json.dumps(track_process.__dict__, indent=4)
    response = None
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.put(uri, data=track_process_req,headers=headers)
    except Exception as e:
        print('[STACKTRACE] PUT::REQ_API_SUBITO_MESSAGE: ' + str(e))
        pass
    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent(response, str(response.status_code), 'PUT')
    return response   

def update_page_by_track_process(track_process,page):
    track_process = get_track_object_from_json(track_process)
    track_process.numPage = page
    update_track_process(track_process)

def update_cards_by_track_process(track_process,card, page):
    track_process = get_track_object_from_json(track_process)
    track_process.numCard = card
    track_process.numPage = page
    update_track_process(track_process)

def update_errorStack_by_track_process(track_process, error):
    track_process = get_track_object_from_json(track_process)
    track_process.errorStack = error
    update_track_process(track_process)

def update_options_by_track_process(track_process, options):
    track_process = get_track_object_from_json(track_process)
    track_process.options = options
    update_track_process(track_process)




def get_id_of_last_track_process():
    uri = settings.BASE_URI + settings.PORT + settings.LAST_TRACK
    response = None
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    reponseDecodedUtf8 = response.content.decode('utf-8')
    temp = re.findall(r'\d+', reponseDecodedUtf8)
    response_cleaned = list(map(int, temp))
    if not response_cleaned:
        return None
    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent('NO', str(response.status_code),'GET')
    return response_cleaned[0]

def get_track_process_by_id(id):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_TRACK + str(id)
    response = None # TODO delete just a try
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    if response.status_code == 400 or response.status_code == 500:
        print_responseNoIndent('NO', str(response.status_code),'GET')
    return response.content

