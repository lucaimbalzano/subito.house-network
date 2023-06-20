# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from service.request import req_api_house  as req


def house_service(data_house):
    response = req.insert_house_request(data_house)
    if response.status_code != 400 and response.status_code != 404:
        if '404-' not in data_house.number:
            print('x')
        else:
            print('y')