import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from request import req_api_subito_message  as req
from tests.messages.test_message import number_msg_and_cont_test
from settings import settings_message
from time import sleep
from urllib.parse import quote
import os

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



    

def send_message_whatsapp(data_immobile_list_by_page):
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=getOptionsWhatsappDriver())
    browser.get('https://web.whatsapp.com')
    
    # TODO do it every run the first time
    # input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
    sleep(15)

    delay = 15
    cont_test = 0
    number_test =''
    total_messages_sent = 0
    try:
        for index_page in range(0, len(data_immobile_list_by_page)):
            for index_house in range(0, len(data_immobile_list_by_page[index_page])):
                response = req.post_api_subito(data_immobile_list_by_page[index_page][index_house])
                if response.status_code != 400 and response.status_code != 404:
                    number = data_immobile_list_by_page[index_page][index_house].number
                    msg_from_settings_message = data_immobile_list_by_page[index_page][index_house].number +'\n'+ settings_message.MSG_INTRO_RENT_01 + data_immobile_list_by_page[index_page][index_house].url + settings_message.MSG_PROPOSAL_RENT_01 + settings_message.PDR_EXAMPLE + settings_message.MSG_TIME_APPOINTMENT_02


                    if cont_test == 5:
                        cont_test = 0
                    if cont_test == 0:
                        number_test = '3273998959'
                    if cont_test == 1:
                        number_test = '3273998959'
                    if cont_test == 2:
                        number_test = '3476970147'
                    if cont_test == 3:
                        number_test = '3396495293'
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
                                    total_messages_sent+=1
                                sent=True
                                sleep(3)
                                print(style.GREEN + 'Message sent to: ' + number + style.RESET)

                            except Exception as e:
                                print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
                                print("Make sure your phone and computer is connected to the internet.")
                                print("If there is an alert, please dismiss it.\n" + style.RESET)
                                if checkAlertInvalidNumber(browser) == 1:
                                    print('[ERROR] Error occured, this number is invalid, couldn''t send a message by whatsapp web \n ➡️   number: '+data_immobile_list_by_page[index_page][index_house].number+', url: '+data_immobile_list_by_page[index_page][index_house].url+' \n' )
                                    break
                        else:
                            break
                            
    except Exception as e:
            traceback.print_exc()
            pass
    print('[DEBUG] total messages sent: '+str(total_messages_sent))
    browser.close()