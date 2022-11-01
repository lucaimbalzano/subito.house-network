# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from asyncio.log import logger
import sys
import time
import traceback

from data_immobile import Data_immobile
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from request.dto.house_request_dto import HouseRequestDTO
from settings import settings

linkForNewTab = ''
linksNotFound = []
numberNotFound = []
house = None;
houseList = []
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


def scrollByPage(browser, num_pages_to_scroll, index_start_num_cards_to_scroll):
    browser.get(settings.BASE_LINK_RENT_HOUSE + str(1) + settings.TIPOLOGY_ADVERTISER_FILTER)
    time.sleep(1)
    data_immobile_pages = []

    for index_page in range(0, num_pages_to_scroll):
        print("[DEBUG] retrieving data from " + str(index_page) + " page")
        data_immobile = scrapingFromUrl(browser, index_page, index_start_num_cards_to_scroll)
        if data_immobile is not None:
            data_immobile_pages.append(data_immobile)
        else:
            return data_immobile_pages
    return data_immobile_pages

def getVetrinaByCard(all_links_cards, index_cards):
    if all_links_cards[index_cards].accessible_name.find('VETRINA') != -1:
        print('[DEBUG] VETRINA house, url: ' + str(all_links_cards[index_cards].get_attribute('href')))
        return True
    else:
        return False

def scrapingFromUrl(browser, index_page, index_start_num_cards):
    browser.get(getUrlHousesListPage(index_page))
    all_links_cards = browser.find_elements(By.CLASS_NAME, "BigCard-module_link__kVqPE")
    if len(all_links_cards) == 0:
        return houseListByPage
   
    try:

        # TODO len(all_links_cards)     
        len_all_links_cards = 5
        for index_cards in range(index_start_num_cards, len_all_links_cards):
            print("[DEBUG] retrieving data from card " + str(index_cards))
            houseList = []

            # TODO for when i'll handle also sell
            advertising_field = 'RENT'
            vetrina_field = getVetrinaByCard(all_links_cards, index_cards)
            urlHouseDetail = all_links_cards[index_cards].get_attribute('href')
            scrapeHouseDetailFromNewTab(browser, urlHouseDetail, vetrina_field, advertising_field)
            
            houseListByPage.append(houseList)
        return houseListByPage      

    # TODO check-double this ex handling
    except NoSuchElementException:
        traceback.print_exc()
        linksNotFound.append(linkForNewTab)
    finally:
        return houseListByPage


def openAndSaveNetTabPosition(browser, url):
    tab_saved = browser.window_handles[0]
    browser.execute_script('window.open("' + url + '");')
    browser.switch_to.window(browser.window_handles[1])
    return tab_saved

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

    # TODO check if  house_features[N] is the proper position
    space_scraped = house_features[0].text.split('\n')[1] if house_features[0].text.split('\n')[1] != '-' else 'NOT SPECIFIED'
    floor_scraped = house_features[2].text.split('\n')[1] if house_features[2].text.split('\n')[1] != '-' else 'NOT SPECIFIED'
    rooms_scraped = house_features[1].text.split('\n')[1] if house_features[1].text.split('\n')[1] != '-' else 'NOT SPECIFIED'
    bathroom_scraped = house_features[3].text.split('\n')[1] if house_features[3].text.split('\n')[1] != '-' else 'NOT SPECIFIED'
    # status_house_scraped =  house_features[4].text.split('\n')[1] if house_features[4].text.split('\n')[1] != '-' else 'NOT SPECIFIED'
    parking_scraped = house_features[5].text.split('\n')[1] if house_features[5].text.split('\n')[1] != '-' else 'NOT SPECIFIED'

    try:
        energy_features = browser.find_element(By.CLASS_NAME, "feature-list_list__UNF-4c").text.split('\n')
        energyHeating_scraped = energy_features[1] if energy_features[1] != '-' else 'NOT SPECIFIED'
        energyClass_scraped = energy_features[3] if energy_features[3] != '-' else 'NOT SPECIFIED'
    except Exception as e:
        logger.error('[ERROR] energy features error occurred: not found')
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


def getNumber(browser):
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
        return 0


def scrapeHouseDetailFromNewTab(browser, url, vetrina_field, advertising_field):
    pin_tab = openAndSaveNetTabPosition(browser, url)
    try:
        number_scraped = getNumber(browser)
        title_scraped = browser.find_element(By.CLASS_NAME, "AdInfo_ad-info__title__7jXnY").text
        price_scraped = browser.find_element(By.CLASS_NAME, "index-module_large__SUacX").text
        name_scraped = browser.find_element(By.CLASS_NAME, "index-module_name__hRS5a").text
        description_scraped = browser.find_element(By.CLASS_NAME, "index-module_preserve-new-lines__ZOcGy").text
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
