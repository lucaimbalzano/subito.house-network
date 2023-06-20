# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import json
import traceback

import requests
from service.request.dto.message_request_dto import MessageRequestDTO
import settings.settings_api as settings
from service.request.dto.house_request_dto import HouseRequestDTO, HouseRequestDTOEncoder
import random


def print_response(response,status_code, request_type):
    print('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    print('STATUS CODE: '+status_code)
    print('BODY REPOSNE: '+str(json.dumps(response,indent=4)))

def print_responsetext(response,status_code, request_type):
    print('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    print('STATUS CODE: '+status_code)
    print('BODY REPOSNE: '+json.dumps(response.text,indent=4))

def print_responseNoIndent(response,status_code, request_type):
    print('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    print('STATUS CODE: '+status_code)
    # print('BODY REPOSNE: '+response.text)

def insert_message(message_dto):
    uri = settings.BASE_URI + settings.PORT + settings.POST_MSG
    
    message_dto =  MessageRequestDTO(message_dto.messageName,message_dto.dateAdded,message_dto.message,message_dto.numberSent)
    message_req_dto = json.dumps(message_dto.__dict__, indent=4)
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.post(uri, data=message_req_dto,headers=headers)
    except Exception as e:
        print('[STACKTRACE] POST::REQ_API_SUBITO_MESSAGE: ' + str(e))
        pass

    print_responseNoIndent(response, str(response.status_code), 'POST')
    return response    