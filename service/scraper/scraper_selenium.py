# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from asyncio.log import logger
import sys
import time
import traceback
import random

from bs4 import BeautifulSoup
import requests
import service.request.req_api_track as req_api_track
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from service.request.dto.house_request_dto import HouseRequestDTO
from service.scraper.exceptions.nosuchelement_house_feature import exception_NoSuchElementExeption_house_ByFieldFinder, exception_NoSuchElementExeption_house_ByFieldFinder_asList, exception_NoSuchElementExeption_house_ByFieldFinder_byGetAttribute
from settings import settings, settings_message
from settings.settings_subito_find_element import SUBITO_FEATURES_HOUSE_ID_NAME, SUBITO_PRICE_HOUSE_CLASS_NAME,SUBITO_NAME_USER_CLASS_NAME, SUBITO_DESC_HOUSE_CLASS_NAME, SUBITO_LOCATION_DISPLAYED_HOUSE_CLASS_NAME, SUBITO_FEATURES_HOUSE_CLASS_NAME,SUBITO_TITLE_HOUSE_CLASS_NAME, SUBITO_ENERGY_FEATURES_CLASS_NAME, SUBITO_USER_URL_PROFILE_CLASS_NAME
from service import house_service

linkForNewTab = ''
linksNotFound = []
numberNotFound = []
house = None;
houseListByPage = []
counter_msg_AorB = 0
count_vetrina = 0
last_track_process = req_api_track.get_track_process_by_id(req_api_track.get_id_of_last_track_process())



def login(browser):
    browser.get(settings.LOGIN_SECTION_SUBITO)
    time.sleep(4)
    privacy_alert = browser.find_element(By.ID, 'didomi-notice-agree-button')
    if privacy_alert != None:
        browser.execute_script("arguments[0].click();", privacy_alert)

    username = browser.find_element("xpath", "//input[@name='username']")
    password = browser.find_element("xpath", "//input[@name='password']")
    username.send_keys(settings.LOGIN_USERNAME)
    password.send_keys(settings.LOGIN_PASSWORD)
    time.sleep(2)
    submit = browser.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(4)


def getUrlHousesListPage(number_page, adv):
    if adv == 'RENT': 
        return settings.BASE_LINK_RENT_HOUSE + str(number_page) + settings.TIPOLOGY_ADVERTISER_FILTER
    else:
        return settings.BASE_LINK_SALE_HOUSE + str(number_page) + settings.TIPOLOGY_ADVERTISER_FILTER

def getIfNOTSPECIFIEDfield(field_retived):
    return field_retived if field_retived != '' else 'NOT SPECIFIED'

def getVetrinaByCard(all_links_cards, index_cards):
    if all_links_cards[index_cards].accessible_name.find('VETRINA') != -1:
        print('[DEBUG] VETRINA house, url: ' + str(all_links_cards[index_cards].get_attribute('href')))
        return True
    else:
        return False


def openAndSaveNetTabPosition(browser, url):
    tab_saved = browser.window_handles[0]
    browser.execute_script('window.open("' + url + '");')
    browser.switch_to.window(browser.window_handles[1])
    return tab_saved



perno = False

def scrollByPage(browser, num_pages_to_scroll, index_start_num_cards_to_scroll, adv):
    if adv == 'RENT':
        browser.get(settings.BASE_LINK_RENT_HOUSE + str(1) + settings.TIPOLOGY_ADVERTISER_FILTER)
        time.sleep(1)
    else:
        browser.get(settings.BASE_LINK_SALE_HOUSE + str(1) + settings.TIPOLOGY_ADVERTISER_FILTER)
        time.sleep(1)
    global perno
    if perno != True:
        perno = True
        privacy_alert = browser.find_element(By.ID, 'didomi-notice-agree-button')
        if privacy_alert != None:
            browser.execute_script("arguments[0].click();", privacy_alert)

    for index_page in range(1, num_pages_to_scroll):
        print("[DEBUG] retrieving data from " + str(index_page) + " page =========================================================================")
        req_api_track.update_page_by_track_process(last_track_process, str(index_page))

        houseList = []
        checkHouseListPage = scrapingFromUrl(browser, index_page, index_start_num_cards_to_scroll, houseList, adv)
        if checkHouseListPage == 0:
            browser.close()
            return houseListByPage
    
    browser.close()
    return houseListByPage



def scrapingFromUrl(browser, index_page, index_start_num_cards, houseList, advertising_from_input):
    browser.get(getUrlHousesListPage(index_page, advertising_from_input))
    print('[DEBUG] url page: '+str((getUrlHousesListPage(index_page, advertising_from_input))))

    all_links_cards = browser.find_elements(By.CLASS_NAME, "BigCard-module_link__kVqPE")
    if len(all_links_cards) == 0:
        return 0
   
    try:
        global count_vetrina
        for index_cards in range(index_start_num_cards, len(all_links_cards)):
            print("[DEBUG] retrieving data from card " + str(index_cards))
            req_api_track.update_cards_by_track_process(last_track_process, str(index_cards), str(index_page))
        
            advertising_field = advertising_from_input
            vetrina_field = getVetrinaByCard(all_links_cards, index_cards)
            urlHouseDetail = all_links_cards[index_cards].get_attribute('href')
            
            # url_soap = requests.get(urlHouseDetail)
            # soup = BeautifulSoup(url_soap, 'html.parser')
            # print(soup.prettify)

            print('[DEBUG] card url: '+ str(urlHouseDetail))
            if vetrina_field and count_vetrina <= 2:
                count_vetrina += 1
                scrapeHouseDetailFromNewTab(browser, urlHouseDetail, vetrina_field, advertising_field, houseList)    
            elif vetrina_field == False:
                scrapeHouseDetailFromNewTab(browser, urlHouseDetail, vetrina_field, advertising_field, houseList)    

        return houseListByPage.append(houseList)    
    except Exception as e:
        traceback.print_exc()
        linksNotFound.append(linkForNewTab)
    finally:
        return houseListByPage


def getFeaturesHouse(browser,
                        location_scraped,
                        house_features,
                        name_scraped,
                        price_scraped,
                        description_scraped,
                        title_scraped,
                        url,
                        number_scraped,
                        vetrina_field,
                        advertising_field):
    
    energyHeating_scraped = 'NOT SPECIFIED'
    energyClass_scraped = 'NOT SPECIFIED'

    space_scraped = ''
    floor_scraped = ''
    rooms_scraped = ''
    bathroom_scraped = ''
    parking_scraped = ''
    status_house_scraped = ''

    if house_features == None:
        house_features = '0'
    for index_field in range(0, len(house_features)):
        field = house_features[index_field]
        if house_features[index_field] == 'Stato':
            status_house_scraped =  house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'
        if house_features[index_field]  == 'Superficie':
            space_scraped =  house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'
        if house_features[index_field]  == 'Piano':
            floor_scraped =  house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'
        if house_features[index_field]  == 'Locali':
            rooms_scraped =  house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'
        if house_features[index_field]  == 'Bagni':
            bathroom_scraped =  house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'
        if house_features[index_field]  == 'Parcheggio':
            parking_scraped =  house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'
        if house_features[index_field]  == 'Classe energetica':
            energyClass_scraped = house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'
        if house_features[index_field]  == 'Riscaldamento':
            energyHeating_scraped = house_features[index_field+1] if house_features[index_field+1] != '-' else 'NOT SPECIFIED'

    try:
        # if energyHeating_scraped == 'NOT SPECIFIED' or energyClass_scraped == 'NOT SPECIFIED':
        #     energy_features = browser.find_element(By.CLASS_NAME, "feature-list_list__UNF-4c").text.split('\n')
        #     energyHeating_scraped = energy_features[1] if energy_features[1] != '-' else 'NOT SPECIFIED'
        #     energyClass_scraped = energy_features[3] if energy_features[3] != '-' else 'NOT SPECIFIED'
                # TODO
        # elevator = browser.find_element(By.ID, 'feature-list-section_detail-chip-container__by96k').text.find('Asce') 
        # balcony and other details
        
        urlProfile_scraped = exception_NoSuchElementExeption_house_ByFieldFinder_byGetAttribute(browser,By.CLASS_NAME,SUBITO_USER_URL_PROFILE_CLASS_NAME,'href')
        if urlProfile_scraped is not None:
            urlProfile_scraped_clean = urlProfile_scraped if urlProfile_scraped != '-' else 'NOT SPECIFIED'
        
    except NoSuchElementException as nsee:
        print(nsee)
        pass
    
        

    return HouseRequestDTO(name_scraped, 
                        price_scraped, 
                        space_scraped, 
                        rooms_scraped, 
                        floor_scraped, 
                        description_scraped, 
                        title_scraped, 
                        url, 
                        number_scraped, 
                        vetrina_field, 
                        advertising_field,
                        bathroom_scraped, 
                        parking_scraped,
                        energyClass_scraped,
                        energyHeating_scraped,
                        urlProfile_scraped_clean,
                        location_scraped
                    )


def getNumberOrContatta(browser):
    try:
        global counter_msg_AorB
        all_buttons_new_tab = browser.find_elements(By.CLASS_NAME, "index-module_icon-only__gkRU8")
        chiama_btn = [btn for btn in all_buttons_new_tab if btn.text == "Contatta"]
        index_all_buttons = all_buttons_new_tab.index(chiama_btn[1])

        if len(chiama_btn) > 0 and int(index_all_buttons) == 6:
            all_buttons_new_tab[int(index_all_buttons) - 1].click()
            time.sleep(1)
            if len(browser.find_elements(By.CLASS_NAME, "index-module_isVisible__GstjN")) == 1:
                number_scraped = browser.find_elements(By.CLASS_NAME, "index-module_isVisible__GstjN")[0].text
                number_scraped_editing = number_scraped.replace("Numero di telefono", "")
                return number_scraped_editing.replace("\n", "")
            else:
                numberNotFound.append(linkForNewTab)
                return 0
        else:
            # if len(chiama_btn) > 0 :
            #     chiama_btn[0].click()
            #     time.sleep(4)
            #     txtAreaContatta = browser.find_element(By.CLASS_NAME, 'index-module_weight-book__AVaSr')
            #     txtAreaContatta.clear()
            #     name = browser.find_element(By.CLASS_NAME, "index-module_name__hRS5a").text
                
            #     testo = ''
            #     if counter_msg_AorB %2 == 0:
            #         testo =  'Ciao'+ ( ' '+name+', ' if ('utente' or 'Utente') not in name else ', ') +settings_message.MSG_INTRO_SALE_02_A_00+'\n\n'+settings_message.MSG_COPY_SALE_02_A01+'\n'+settings_message.MSG_COPY_SALE_02_A02+'\n'+settings_message.MSG_COPY_SALE_02_A03+'\n\n'+settings_message.MSG_COPY_SALE_02_A04+'\n\n'+settings_message.MSG_COPY_SALE_02_A05+settings_message.MSG_COPY_SALE_02_A06+'\n'+settings_message.MSG_COPY_SALE_02_A07+'\n'+settings_message.MSG_COPY_SALE_02_A08+'\n\n'+settings_message.MSG_COPY_SALE_02_A09+'\n'+settings_message.FOLDER_DOCS_FREE_CONTENT+'\n\n'+settings_message.MSG_COPY_SALE_02_A10+'\nSimone'
            #         counter_msg_AorB += 1
            #     else:
            #         testo =  settings_message.MSG_INTRO_SALE_03_A00+'\n\n'+settings_message.MSG_COPY_SALE_03_A01+'\n\n'+settings_message.MSG_COPY_SALE_03_A02+'\n'+settings_message.MSG_COPY_SALE_03_A02_A+'\n\n'+settings_message.MSG_COPY_SALE_03_A03+'\n'+settings_message.FOLDER_DOCS_FREE_CONTENT+'\n\n'+settings_message.MSG_COPY_SALE_03_A04+'\n'+settings_message.MSG_COPY_SALE_03_A05+'\n'+settings_message.MSG_COPY_SALE_03_A06+'\n\n'+settings_message.MSG_COPY_SALE_03_A08+'\n\n'+settings_message.MSG_COPY_SALE_03_A09+'\n\n'+settings_message.MSG_COPY_SALE_03_A10+'\nSimone'
            #         counter_msg_AorB += 1

            #     txtAreaContatta.send_keys(testo)
            #     browser.find_element(By.CLASS_NAME, 'form-module_submitButton__HaEyv').click()

            #     time.sleep(2)
            return 0
    except Exception as e:
        print('[ERROR] Error occurred during scraping number: ' + str(e))
        traceback.print_exc()
        # req_api_track.update_errorStack_by_track_process(last_track_process, e)
        pass


def scrapeHouseDetailFromNewTab(browser, url, vetrina_field, advertising_field, houseList):
    pin_tab = openAndSaveNetTabPosition(browser, url)
      
    number_scraped = getNumberOrContatta(browser)
    if number_scraped == 0 or number_scraped == None:
        number_scraped = '404-' + str(random.randrange(999, 999999))

    title_scraped = exception_NoSuchElementExeption_house_ByFieldFinder(browser, By.CLASS_NAME,SUBITO_TITLE_HOUSE_CLASS_NAME,1) if True else 'NOT SPECIFIED' 
    price_scraped = exception_NoSuchElementExeption_house_ByFieldFinder(browser, By.CLASS_NAME ,SUBITO_PRICE_HOUSE_CLASS_NAME,1) if True else 'NOT SPECIFIED'
    name_scraped = exception_NoSuchElementExeption_house_ByFieldFinder(browser, By.CLASS_NAME ,SUBITO_NAME_USER_CLASS_NAME,1) if True else 'NOT SPECIFIED'
    description_scraped = exception_NoSuchElementExeption_house_ByFieldFinder(browser, By.CLASS_NAME ,SUBITO_DESC_HOUSE_CLASS_NAME,1) if True else 'NOT SPECIFIED'
    location_scraped = exception_NoSuchElementExeption_house_ByFieldFinder(browser, By.CLASS_NAME ,SUBITO_LOCATION_DISPLAYED_HOUSE_CLASS_NAME,1)  if True else 'NOT SPECIFIED'
    # house_features = exception_NoSuchElementExeption_house_ByFieldFinder_asList(browser, By.CLASS_NAME ,SUBITO_FEATURES_HOUSE_CLASS_NAME,0)  if True else 'NOT SPECIFIED'
    house_features = exception_NoSuchElementExeption_house_ByFieldFinder_asList(browser, By.ID ,SUBITO_FEATURES_HOUSE_ID_NAME,1).split('\n')
    # if True else 'NOT SPECIFIED'

    house = getFeaturesHouse(browser,
                            location_scraped,
                            house_features,
                            name_scraped,
                            price_scraped,
                            description_scraped,
                            title_scraped,
                            url,
                            number_scraped,
                            vetrina_field,
                            advertising_field)

    if house is not None:
        house_service(house)
        houseList.append(house)

    browser.close()
    browser.switch_to.window(pin_tab)
