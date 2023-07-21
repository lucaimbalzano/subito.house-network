# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from os import system
import traceback
import time
# import pyautogui as pg 
# from pyautogui import hotkey
# import pywhatkit as pwk
from datetime import datetime
from service.request import req_api_house  as req
import keyboard
import time



from settings import settings_message
from tests.messages.test_message import number_msg_and_cont_test


def whatmsg(telef, msg):
#   pwk.sendwhatmsg_instantly(telef, msg)
  time.sleep(2)
#   pg.click()
  time.sleep(1)


  keyboard.press_and_release('enter')


def send_message(data_immobile_list_by_page):
    cont_msg = 0
    cont_test = 0
    number_test =''
    try:                             
        for index_page in range(0, len(data_immobile_list_by_page)):
            for index_house in range(0, len(data_immobile_list_by_page[index_page])):
                
            
                response = req.insert_house_request(data_immobile_list_by_page[index_page][index_house])

                if response.status_code != 400 and response.status_code != 404:
                    msg_from_settings_message = data_immobile_list_by_page[index_page][index_house].number +'\n'+ settings_message.MSG_INTRO_RENT_01 + data_immobile_list_by_page[index_page][index_house].url + settings_message.MSG_PROPOSAL_RENT_01 + settings_message.PDR_EXAMPLE_AIRBNB + settings_message.MSG_TIME_APPOINTMENT_02
                    
                    number_msg_and_cont_test(cont_test, number_test)

                    

                    
                    # pwk.sendwhatmsg_instantly(settings_message.PREFIX_ITA + number_test, 
                    #                             msg_from_settings_message , 
                    #                             wait_time=5, 
                    #                             tab_close=True)

                    whatmsg(settings_message.PREFIX_ITA + number_test, msg_from_settings_message)

                    # pwk.sendwhatmsg_instantly(settings_message.PREFIX_ITA + number_test, msg_from_settings_message,tab_close=True)

                    # keyboard.press_and_release('ctrl+w')
                    time.sleep(2)
                    cont_msg+=1



                    
                    break
            break

    except Exception as e: 
        traceback.print_exc()

        

        
        

        print(str(e))

        
        print("Error in sending the message, "+str(e))

    