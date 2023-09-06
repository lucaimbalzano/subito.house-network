# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import json
from logging import getLogger
import traceback

import requests
import settings.settings_api as settings
from service.request.dto.house_request_dto import HouseRequestDTO, HouseRequestDTOEncoder
import random

logger = getLogger()

def print_response(response,status_code, request_type, url_house, number):
    logger.debug('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    logger.debug('STATUS CODE: '+status_code)
    if number != 0:
        logger.debug('NUMBER: '+number)
    logger.debug('URL HOUSE: '+url_house)
    # logger.debug('BODY REPOSNE: '+str(json.dumps(response,indent=4)))
    # TODO delete
    logger.debug(' ')

def print_responsetext(response,status_code, request_type):
    logger.debug('[DEBUG] '+request_type+'::HTTP-RESPONSE: ')
    logger.debug('STATUS CODE: '+status_code)
    # logger.debug('BODY REPOSNE: '+json.dumps(response.text,indent=4))
    # TODO delete
    logger.debug(' ')

def insert_house_request(house_dto):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_HOUSE_REQ
    house_req_dto = json.dumps(house_req_dto.__dict__, indent=4)
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.post(uri, data=house_req_dto,headers=headers)
    except Exception as e:
        logger.debug('[STACKTRACE] POST::REQ_API_SUBITO_MESSAGE: ' + str(e))
        pass

    print_response(response.json(), str(response.status_code), 'POST', house_dto.url, house_dto.number)
    return response    

def get_api_subito(id_house):
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBITO_REQ + id_house
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        logger.debug('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    print_response(response.json(), str(response.status_code),'GET')

def get_api_subito_all_houses():
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBITO_REQ
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        logger.debug('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    print_response(response.json(), str(response.status_code),'GET')
    return response


def get_api_subito_check_number(number_house):
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBIOT_CHECK_REQ + number_house
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        logger.debug('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
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
        logger.debug('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    
    print_response(response.json(), str(response.status_code),'GET')
    return response
 
def get_api_subito_check_number_adv(number_house, adv_house):
    
    uri = settings.BASE_URI + settings.PORT + settings.GET_SUBITO_CHECK_ADV_BY_NUMBER_REQ + number_house + '/' + adv_house
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.get(uri)
    except Exception as e:
        logger.debug('[STACKTRACE] GET::REQ_API_SUBITO_MESSAGE: ' + str(e))
    if response.text == '':
        print_responsetext(response, '404','GET')
    else:
        print_responsetext(response, '200','GET')
    return response.text

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