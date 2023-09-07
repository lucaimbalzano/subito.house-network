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
    logger.debug(request_type+' - '+str(status_code))
    if number != 0:
        logger.debug(request_type+' - '+str(status_code)+', NUMBER: '+number+', URL HOUSE: '+url_house)
    logger.debug(request_type+' - '+str(status_code)+', URL HOUSE: '+url_house)

def print_responsetext(response,status_code, request_type):
    logger.debug(request_type+' - '+str(status_code))

def insert_house_request(house_dto):
    uri = settings.BASE_URI + settings.PORT + settings.CRUD_HOUSE_REQ
    house_req_dto = json.dumps(house_dto.__dict__, indent=4)
    
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.post(uri, data=house_req_dto,headers=headers)
    except Exception as e:
        logger.debug('[STACKTRACE] POST::REQ_API_SUBITO_MESSAGE: ' + str(e))
        pass

    print_response(response.json(), response.status_code, 'POST', house_dto.url, house_dto.number)
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
