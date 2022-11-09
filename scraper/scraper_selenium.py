# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from asyncio.log import logger
import sys
import time
import traceback
import random

from data_immobile import Data_immobile
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from request.dto.house_request_dto import HouseRequestDTO
from settings import settings

linkForNewTab = ''
linksNotFound = []
numberNotFound = []
house = None;
houseListByPage = []





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


def getUrlHousesListPage(number_page):
    return settings.BASE_LINK_RENT_HOUSE + str(number_page) + settings.TIPOLOGY_ADVERTISER_FILTER

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










def scrollByPage(browser, num_pages_to_scroll, index_start_num_cards_to_scroll, adv):
    if adv == 'RENT':
        browser.get(settings.BASE_LINK_RENT_HOUSE + str(1) + settings.TIPOLOGY_ADVERTISER_FILTER)
        time.sleep(1)
    else:
        browser.get(settings.BASE_LINK_SALE_HOUSE + str(1) + settings.TIPOLOGY_ADVERTISER_FILTER)
        time.sleep(1)

    for index_page in range(0, num_pages_to_scroll):
        print("[DEBUG] retrieving data from " + str(index_page) + " page")
       
        houseList = []
        checkHouseListPage = scrapingFromUrl(browser, index_page, index_start_num_cards_to_scroll, houseList, adv)
        if checkHouseListPage == 0:
            return houseListByPage
            
    return houseListByPage



def scrapingFromUrl(browser, index_page, index_start_num_cards, houseList, advertising_from_input):
    browser.get(getUrlHousesListPage(index_page))
    print('[DEBUG] url page: '+str((getUrlHousesListPage(index_page))))

    all_links_cards = browser.find_elements(By.CLASS_NAME, "BigCard-module_link__kVqPE")
    if len(all_links_cards) == 0:
        return 0
   
    try:
        for index_cards in range(index_start_num_cards,  len(all_links_cards)):
            print("[DEBUG] retrieving data from card " + str(index_cards))
            # TODO for when i'll handle also sell
            advertising_field = advertising_from_input
            vetrina_field = getVetrinaByCard(all_links_cards, index_cards)
            urlHouseDetail = all_links_cards[index_cards].get_attribute('href')
            print('[DEBUG] card url: '+ str(urlHouseDetail))
            scrapeHouseDetailFromNewTab(browser, urlHouseDetail, vetrina_field, advertising_field, houseList)
            
        return houseListByPage.append(houseList)    

    # TODO check-double this ex handling
    except NoSuchElementException:
        traceback.print_exc()
        linksNotFound.append(linkForNewTab)
    finally:
        return houseListByPage


def getFeaturesHouse(browser,
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

    for index_field in range(0, len(house_features)):
        field = house_features[index_field].text.split('\n')   
        if field[0] == 'Stato':
            status_house_scraped =  field[1] if field[1] != '-' else 'NOT SPECIFIED'
        if field[0] == 'Superficie':
            space_scraped =  field[1] if field[1] != '-' else 'NOT SPECIFIED'
        if field[0] == 'Piano':
            floor_scraped =  field[1] if field[1] != '-' else 'NOT SPECIFIED'
        if field[0] == 'Locali':
            rooms_scraped =  field[1] if field[1] != '-' else 'NOT SPECIFIED'
        if field[0] == 'Bagni':
            bathroom_scraped =  field[1] if field[1] != '-' else 'NOT SPECIFIED'
        if field[0] == 'Parcheggio':
            parking_scraped =  field[1] if field[1] != '-' else 'NOT SPECIFIED'


    try:
        energy_features = browser.find_element(By.CLASS_NAME, "feature-list_list__UNF-4c").text.split('\n')
        energyHeating_scraped = energy_features[1] if energy_features[1] != '-' else 'NOT SPECIFIED'
        energyClass_scraped = energy_features[3] if energy_features[3] != '-' else 'NOT SPECIFIED'
    except Exception as e:
        # logger.error('[ERROR] energy features error occurred: not found')
        sys.exc_clear()
        pass
    finally:
        # elevator = browser.find_element(By.ID, 'feature-list-section_detail-chip-container__by96k').text.find('Asce') 
        urlProfile_scraped = browser.find_element(By.CLASS_NAME, "index-module_rounded_user_badge__KC3zi").get_attribute('href')
        urlProfile_scraped_clean = urlProfile_scraped if urlProfile_scraped != '-' else 'NOT SPECIFIED'

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
                            urlProfile_scraped_clean
                        )


def getNumberOrContatta(browser):
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
        if len(chiama_btn) > 0 :
            chiama_btn[0].click()
            time.sleep(2)
            txtAreaContatta = browser.find_element(By.CLASS_NAME, 'index-module_weight-book__AVaSr')
            txtAreaContatta.clear() 
            testo = 'Buonanotte a te, buonanotte a me, buonanotte a chi ancora non ho incontrato\n'+'Buonanotte pure a lei\n'+'Anche oggi che ti vorrei semplicemente\n'+'Semplicemente\n'+'Semplicemente\n'+'(Nananana)\n'
            txtAreaContatta.send_keys(testo)
            browser.find_element(By.CLASS_NAME, "index-module_icon-only__gkRU-2").click()
            time.sleep(2)
        return 0


def scrapeHouseDetailFromNewTab(browser, url, vetrina_field, advertising_field, houseList):
    pin_tab = openAndSaveNetTabPosition(browser, url)
    try:
        number_scraped = getNumberOrContatta(browser)
        if number_scraped == 0:
            number_scraped = '404-' + str(random.randrange(999, 999999))

        title_scraped = browser.find_element(By.CLASS_NAME, "AdInfo_ad-info__title__7jXnY").text
        title_scraped = getIfNOTSPECIFIEDfield(title_scraped)

        price_scraped = browser.find_element(By.CLASS_NAME, "index-module_large__SUacX").text
        price_scraped = getIfNOTSPECIFIEDfield(price_scraped)

        name_scraped = browser.find_element(By.CLASS_NAME, "index-module_name__hRS5a").text
        name_scraped = getIfNOTSPECIFIEDfield(name_scraped)

        description_scraped = browser.find_element(By.CLASS_NAME, "index-module_preserve-new-lines__ZOcGy").text
        description_scraped = getIfNOTSPECIFIEDfield(description_scraped)

        house_features = browser.find_elements(By.CLASS_NAME, "feature-list_feature__8a4rn")
        house = getFeaturesHouse(browser, 

        
                                house_features,
                                name_scraped,
                                price_scraped,
                                description_scraped,
                                title_scraped,
                                url,
                                number_scraped,
                                vetrina_field,
                                advertising_field)
        

    except NoSuchElementException:
        print('--- Error occurred, Title Apartment: ' + str(title_scraped) + '; URL: ' + str(url))
        pass

    finally:
        houseList.append(house)

        browser.close()
        browser.switch_to.window(pin_tab)
