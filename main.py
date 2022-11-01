# coding=utf-8

from email import *
from browser.browser import Browser
from messages import send_message_by_data_house
from response.res_api_subito_message_get_all import HousesListDTO, HousesListDTODecoder
from scraper.scraper_selenium import *
from utils.auxiliary_functions_excel import writeExcelByDataImmobile
from utils.cronometer import ChronoMeter
from request.req_api_subito_message import get_api_subito, get_api_subito_all_houses, get_api_subito_check, post_api_subito
from utils.auxiliary_functions import *
from settings import settings
import json
import traceback
import datetime as dt
import time



def getDataImmobile(link):
    data_immobile = scrapingFromUrl(link)
    return data_immobile

if __name__ == '__main__':
    chrono = ChronoMeter()
    chrono.start_chrono()

    browser = Browser.get_browser()
    login(browser)
    try:
        
        data_immobile_pages = scrollByPage(browser, 3, 0)
        # data_immobile_pages =  Data_immobile(['name'], ['223'], ['85'], ['3'], ['2'], ['description'], ['title_01'], ['url'], ['3345679876'],[False], ['RENT']);
        if data_immobile_pages is not None:
            # write on excel
            post_api_subito(data_immobile_pages)
            send_message_by_data_house.send_message(data_immobile_pages)
        else:
           print("[STACKTRACE] Error __main__:data_immobile_pages  - is None")
           quit()
    except Exception as e:
        traceback.print_exc()
        print('[STACKTRACE] __main__: '+str(e))
        pass



    chrono.stop_chrono()
    chrono.print_time()
    exit(1)

