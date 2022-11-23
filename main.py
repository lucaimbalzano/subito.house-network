# coding=utf-8
# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from email import *
from browser.browser import Browser
from messages import send_message_by_data_house
from messages.send_message_by_data_house_selenium import send_message_whatsapp
from request.req_api_state import get_id_of_last_state_machine_process, get_state_machine_process_by_id, insert_state_machine_process, update_state_machine_process
from request.req_api_track import get_id_of_last_track_process, get_track_process_by_id, insert_track_process, update_track_process
from response.res_api_state import get_state_object_from_json
from response.res_api_subito_message_get_all import HousesListDTO, HousesListDTODecoder
from response.res_api_track import TrackProcessListDTODecoder, get_track_object_from_json
from scraper.scraper_selenium import *
from tests.dto.console import Console, input_console
from tests.dto.test_data_immobile import getHouseListPageTest
from tests.state.state_tests import get_fake_state_machine
from tests.track.track_tests import get_fake_track
from utils.auxiliary_functions_excel import writeExcelByDataImmobile
from utils.cronometer import ChronoMeter
from utils.auxiliary_functions import *
from settings import settings
import json
import traceback
import datetime as dt
import time
import test

from utils.processes_statemachine_track import finish_state_machine_track, init_state_machine_track


def getDataImmobile(link):
    data_immobile = scrapingFromUrl(link)
    return data_immobile

if __name__ == '__main__':
    chrono = ChronoMeter()
    chrono.start_chrono()
    print('V001::SUBITO.HOUSE-NETWORK     - STARTED')
    init_state_machine_track()
    
    try:
    
        # console = input_console()
        #TODO
        console =  Console('2',True,False,False)
        if console.exit:
            print('Exit with sucess')
            pass
        else:
            browser = Browser.get_browser()
            login(browser)
            
            adv = 'RENT' if console.advertising == '1' else 'SALE'
            houseListByPage = scrollByPage(browser, 50, 0, adv)
            
            if houseListByPage is not None:
                if console.excel:
                    print('//TODO write on excel')
                    # write on excel
                if console.message:
                    send_message_whatsapp(houseListByPage)
            else:
                print("[STACKTRACE] Error __main__:data_immobile_pages  - is None")
                quit()
                
    except Exception as e:
        traceback.print_exc()
        print('[STACKTRACE] __main__: '+str(e))
        pass
    
    
    finish_state_machine_track(chrono.current_seconds_time, chrono.current_minutes_time)
    print('V001::SUBITO.HOUSE-NETWORK - ENDED')
    chrono.stop_chrono()
    chrono.print_time()
    exit(1)

