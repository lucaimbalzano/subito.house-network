# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import time
import traceback

from data_immobile import Data_immobile
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from settings import settings





linkForNewTab = ''
linksNotFound = []
numberNotFound = []
nameList,priceList,spaceList, roomsList, floorList, descriptionList, titleList, urlHouseDetailList, numberList, bathList, upload_timeList =[],[],[],[],[],[],[],[],[], [], []


def login(browser):
    browser.get(settings.LOGIN_SECTION_SUBITO)
    time.sleep(4)
    privacy_alert = browser.find_element(By.ID, 'didomi-notice-agree-button')
    if privacy_alert != None:
        browser.execute_script("arguments[0].click();", privacy_alert)

    username = browser.find_element("xpath","//input[@name='username']")
    password = browser.find_element("xpath","//input[@name='password']")
    username.send_keys(settings.LOGIN_USERNAME)
    password.send_keys(settings.LOGIN_PASSWORD)
    time.sleep(2)
    submit = browser.find_element("xpath","//button[@type='submit']").click()
    time.sleep(4)


def getUrlHousesListPage(number_page):
    return settings.BASE_LINK_RENT_HOUSE + str(number_page) + settings.TIPOLOGY_ADVERTISER_FILTER


def scrollByPage(browser):
    browser.get(settings.BASE_LINK_RENT_HOUSE+str(1)+settings.TIPOLOGY_ADVERTISER_FILTER)
    time.sleep(1)
    # TODO CHANGE
    lastPage = 100
    data_immobile_pages = []
    
    for index in range(1, int(lastPage)):
        print("[DEBUG] retrieving data from "+str(index)+" page")
        data_immobile_pages.append(scrapingFromUrl(browser, index))
    return data_immobile_pages

def scrapingFromUrl(browser, index):
    browser.get(getUrlHousesListPage(index))
    all_links_cards = browser.find_elements(By.CLASS_NAME, "BigCard-module_link__kVqPE")
    if all_links_cards is None:
        return Data_immobile(nameList,priceList,spaceList, roomsList, floorList, descriptionList, titleList, urlHouseDetailList, numberList)

    try:
        for index_cards in range(1, len(all_links_cards)):
            print("[DEBUG] retrieving data from card " + str(index_cards))
            urlHouseDetail = all_links_cards[index_cards].get_attribute('href')
            urlHouseDetailList.append(urlHouseDetail)
            scrapeHouseDetailFromNewTab(browser, urlHouseDetail)

    except NoSuchElementException:
        traceback.print_exc()
        linksNotFound.append(linkForNewTab)
    finally:
            return Data_immobile(nameList,priceList,spaceList, roomsList, floorList, descriptionList, titleList, urlHouseDetailList, numberList)

def openAndSaveNetTabPosition(browser, url):
    tab_saved = browser.window_handles[0]
    browser.execute_script('window.open("' + url + '");')
    browser.switch_to.window(browser.window_handles[1])
    return tab_saved

def scrapeHouseDetailFromNewTab(browser, url):
    pin_tab = openAndSaveNetTabPosition(browser, url)

    number_scraped = ''
    title_scraped = browser.find_element(By.CLASS_NAME, "AdInfo_ad-info__title__7jXnY").text
    if "Trilocale arredato mm rogoredo" in title_scraped:
        print("debug")
    price_scraped = browser.find_element(By.CLASS_NAME, "index-module_large__SUacX").text
    name_scraped = browser.find_element(By.CLASS_NAME, "index-module_name__hRS5a").text
    space_rooms_floor = browser.find_elements(By.CLASS_NAME, "MainData_label__4od4v")
    floor_scraped = ''
    rooms_scraped = ''
    space_scraped = ''
    bath_scraped = ''
    # space_scraped = space_rooms_floor[0].text

    for index_details in range(1, len(space_rooms_floor)):
           space_scraped = space_rooms_floor[0].text
           if "agn" in space_rooms_floor[index_details].text:
               bath_scraped = space_rooms_floor[index_details].text
           elif "iano" in space_rooms_floor[index_details].text or "ato" in space_rooms_floor[index_details].text:
               floor_scraped = space_rooms_floor[index_details].text
           elif "cali" in space_rooms_floor[index_details].text:
               rooms_scraped = space_rooms_floor[index_details].text

    description_scraped = browser.find_element(By.CLASS_NAME, "index-module_preserve-new-lines__ZOcGy").text

    try:
        all_buttons_new_tab = browser.find_elements(By.CLASS_NAME, "index-module_icon-only__gkRU8")
        chiama_btn = [btn for btn in all_buttons_new_tab if btn.text == "Contatta"]
        index_all_buttons = all_buttons_new_tab.index(chiama_btn[1])

        if len(chiama_btn) > 0 and int(index_all_buttons) == 6 :
            all_buttons_new_tab[int(index_all_buttons)-1].click()
            time.sleep(1)
            if len(browser.find_elements(By.CLASS_NAME, "index-module_isVisible__GstjN")) == 1:
                number_scraped = browser.find_elements(By.CLASS_NAME, "index-module_isVisible__GstjN")[0].text
                number_scraped_editing = number_scraped.replace("Numero di telefono", "")
                number_scraped = number_scraped_editing.replace("\n", "")
            else:
                numberNotFound.append(linkForNewTab)

    except NoSuchElementException:
        print('--- Error occurred, no number for: '+str(title_scraped)+'; URL: '+str(url))
        pass
    # TODO DELETE
    if number_scraped:
        nameList.append(name_scraped)
        priceList.append(price_scraped)
        spaceList.append(space_scraped)
        roomsList.append(rooms_scraped)
        floorList.append(floor_scraped)
        descriptionList.append(description_scraped)
        titleList.append(title_scraped)
        numberList.append(number_scraped)
        bathList.append(bath_scraped)

    browser.close()
    browser.switch_to.window(pin_tab)




