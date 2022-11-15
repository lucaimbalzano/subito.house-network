import datetime
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from request import req_api_house  as req
from request import req_api_message as req_msg
from request.dto.house_request_dto import HouseRequestDTO
from request.dto.message_request_dto import MessageRequestDTO
from tests.messages.test_message import number_msg_and_cont_test
from settings import settings_message
from time import sleep
from urllib.parse import quote
import os
import hashlib
import json
from types import SimpleNamespace


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



def checkAlertInvalidNumber(browser):
    div_number_invalid_alert = browser.find_element(By.CLASS_NAME, 'gjuq5ydh')
    if div_number_invalid_alert != None:
        browser.execute_script("arguments[0].click();", div_number_invalid_alert)
        return 1
    else:
        return 0



def getOptionsWhatsappDriver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--profile-directory=Default")
    options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
    return options


def getMessageBasedFromADV(adv, data_immobile):
    br = (Keys.SHIFT)+(Keys.SHIFT)
    if adv == 'RENT':
         return f"{data_immobile.number}%0A{settings_message.MSG_INTRO_RENT_01}%0A{data_immobile.url}%0A%0A{settings_message.MSG_PROPOSAL_RENT_01}%0A%0A{settings_message.PDR_EXAMPLE}%0A%20%0A{settings_message.MSG_TIME_APPOINTMENT_RENT_02}"
    else:
         return f"{data_immobile.number}%0A{settings_message.MSG_INTRO_SALE_01}%0A{data_immobile.url}%0A%0A{settings_message.MSG_PROPOSAL_SALE_01}%0A%0A{settings_message.PDR_EXAMPLE}%0A%20%0A{settings_message.MSG_TIME_APPOINTMENT_SALE_02}"


def response_msg_checker(response_msg):
    if response_msg.status_code != 400 and response_msg.status_code != 404:
        print('[DEBUG] message saved on db with success')
    else:
        print('[ERROR] couldnt save message on db, reason: '+response_msg.content)

    

def send_message_whatsapp(data_immobile_list_by_page):
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=getOptionsWhatsappDriver())
    browser.get('https://web.whatsapp.com')
    
    # TODO do it every run the first time
    # input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
    sleep(15)
    # TODO delay
    delay = 15
    cont_test = 0
    number_test =''
    tot_count_msg_in_error = 0
    check_tot_for_api_msg = 0
    total_messages_sent = 0
    try:
        for index_page in range(0, len(data_immobile_list_by_page)):
            for index_house in range(0, len(data_immobile_list_by_page[index_page])):
                response = req.insert_house_request(data_immobile_list_by_page[index_page][index_house])

                if response.status_code != 400 and response.status_code != 404:
                    if '404-' not in data_immobile_list_by_page[index_page][index_house].number:
                     
                        msg_from_settings_message = getMessageBasedFromADV(data_immobile_list_by_page[index_page][index_house].advertising,data_immobile_list_by_page[index_page][index_house])




                        if cont_test == 5:
                            cont_test = 0
                        if cont_test == 0:
                            number_test = '3486049869'
                        if cont_test == 1:
                            number_test = '3474149281'
                        if cont_test == 2:
                            number_test = '3476970147'
                        if cont_test == 3:
                            number_test = '3486049869'
                        if cont_test == 4:
                            number_test = '3474149281'
                        cont_test+=1


                        url = 'https://web.whatsapp.com/send?phone=' + '+39'+number_test + '&text=' + msg_from_settings_message
                        sleep(3)
                        sent = False
                        for i in range(3):
                            if not sent:
                                browser.get(url)
                                try:
                                    click_btn = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                                    sleep(1)
                                    if click_btn is not None:
                                        click_btn.click()
                                        check_tot_for_api_msg = total_messages_sent
                                        total_messages_sent+=1
                                    sent=True
                                    sleep(35)
                                    print(style.GREEN + 'Message sent to: ' + data_immobile_list_by_page[index_page][index_house].number + style.RESET)

                                except Exception as e:
                                    print(style.RED + f"\nFailed to send message to: { data_immobile_list_by_page[index_page][index_house].number}, retry ({i+1}/3)")
                                    print("Make sure your phone and computer is connected to the internet.")
                                    print("If there is an alert, please dismiss it.\n" + style.RESET)
                                    if checkAlertInvalidNumber(browser) == 1:
                                        print('[ERROR] Error occured, this number is invalid, couldn''t send a message by whatsapp web \n ➡️   number: '+data_immobile_list_by_page[index_page][index_house].number+', url: '+data_immobile_list_by_page[index_page][index_house].url+' \n' )
                                        break
                            else:
                                houseCleanedUtf = response.content.decode('utf-8')
                                houseReqByNamesSpace = json.loads(houseCleanedUtf, object_hook=lambda d : SimpleNamespace(**d))
                                if check_tot_for_api_msg < total_messages_sent:
                                    msg_req_dto = MessageRequestDTO(houseReqByNamesSpace.advertising, None, msg_from_settings_message,houseReqByNamesSpace.id)
                                    response_msg = req_msg.insert_message(msg_req_dto)
                                    response_msg_checker(response_msg)
                                    # houseReqDto = req.get_api_subito_check_number_adv(data_immobile_list_by_page[index_page][index_house].number, data_immobile_list_by_page[index_page][index_house].advertising)

                                else:
                                    msg_req_dto = MessageRequestDTO(houseReqByNamesSpace.advertising, None, msg_from_settings_message,houseReqByNamesSpace.id)
                                    response_msg = req_msg.insert_message(msg_req_dto)
                                    print(' ')
                                    response_msg_checker(response_msg)
                                    # houseReqDto = req.get_api_subito_check_number_adv(data_immobile_list_by_page[index_page][index_house].number, data_immobile_list_by_page[index_page][index_house].advertising)
                                    tot_count_msg_in_error += 1
                                    total_messages_sent += 1
                                break
                                
    except Exception as e:
            traceback.print_exc()
            pass
    total_messages_sent = total_messages_sent - tot_count_msg_in_error
    print('[DEBUG] total messages sent: '+str(total_messages_sent))
    # TODO
    print(' ')
    browser.close()