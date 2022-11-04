import json
import traceback

import requests
import settings.settings_api as settings
from data_immobile import Data_immobile
from request.dto.house_request_dto import HouseRequestDTO, HouseRequestDTOEncoder
import random


def print_response(response,status_code, request_type, url_house, number):
    print('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    print('STATUS CODE: '+status_code)
    if number != 0:
        print('NUMBER: '+number)
    print('URL HOUSE: '+url_house)
    print('BODY REPOSNE: '+str(json.dumps(response,indent=4)))

def print_responsetext(response,status_code, request_type):
    print('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    print('STATUS CODE: '+status_code)
    print('BODY REPOSNE: '+json.dumps(response.text,indent=4))

def post_api_subito(house_dto):
    uri = settings.BASE_URI + settings.PORT + settings.POST_SUBITO_REQ
    house_req_dto = HouseRequestDTO(house_dto.name,house_dto.price,house_dto.space,house_dto.rooms,house_dto.floor,house_dto.description,house_dto.title,house_dto.url,house_dto.number,house_dto.vetrina,house_dto.advertising,house_dto.bathrooms, house_dto.parking, house_dto.energyClass, house_dto.energyHeating, house_dto.urlUserProfile)
    house_req_dto = json.dumps(house_req_dto.__dict__, indent=4)
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.post(uri, data=house_req_dto,headers=headers)
    except Exception as e:
        print('[STACKTRACE] POST::REQ_API_SUBITO_MESSAGE: ' + str(e))

    print_response(response.json(), str(response.status_code), 'POST', house_dto.url, house_dto.number)
    return response

    
    

def get_api_subito(id_house):
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBITO_REQ + id_house
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    print_response(response.json(), str(response.status_code),'GET')

def get_api_subito_all_houses():
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBITO_REQ
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    print_response(response.json(), str(response.status_code),'GET')
    return response


def get_api_subito_check(number_house):
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBIOT_CHECK_REQ + number_house
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    if response.text == '':
        print_responsetext(response, '404','GET')
    else:
        print_responsetext(response, '200','GET')
    return response.text

def get_api_subito_all_houses():
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBITO_REQ
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        print('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    print_response(response.json(), str(response.status_code),'GET')
    return response
 


# EXAMPLE REQ
# {
#         "id": 1,
#         "name": "Test01",
#         "price": "200",
#         "space": "100",
#         "rooms": "4",
#         "floor": "3",
#         "bathrooms": "2",
#         "description": "Duomo House",
#         "title": "Title Test01",
#         "parking": "Privato",
#         "energyClass": "A",
#         "energyHeating": "Centralizzato",
#         "urlUserProfile": "https://url_profile",
#         "url": "https://url",
#         "number": "3311011258",
#         "vetrina": false,
#         "advertising": "RENT"
#     },