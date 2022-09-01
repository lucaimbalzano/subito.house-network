# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import time
import traceback

from data_immobile import Data_immobile
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--incognito");
browser = webdriver.Chrome('C:/Users/lucai/Documents/Utils/SW/WebDriver/104/5112/79/chromedriver.exe', chrome_options=options)
browser.get('https://areariservata.subito.it/annunci?login_tooltip=true')
filter_privato = '&advt=0'
linkForNewTab = ''
linksNotFound = []
numberNotFound = []
name,price,space, rooms, floor, description, title, url_list, number, bath, upload_time =[],[],[],[],[],[],[],[],[], [], []


def login():
    time.sleep(4)
    privacy_alert = browser.find_element(By.ID, 'didomi-notice-agree-button')
    if privacy_alert != None:
        browser.execute_script("arguments[0].click();", privacy_alert)

    username = browser.find_element("xpath","//input[@name='username']")
    password = browser.find_element("xpath","//input[@name='password']")
    username.send_keys('lucaimbalzano@gmail.com')
    password.send_keys('Slowspoke00')
    time.sleep(2)
    submit = browser.find_element("xpath","//button[@type='submit']").click()
    time.sleep(4)

def scrapingFromUrl(urlFromMain):

    browser.get(urlFromMain+str(1)+filter_privato)
    time.sleep(1)
    pagination = browser.find_elements(By.CLASS_NAME, "index-module_button-text__VZcja")
    lastPage = pagination[len(pagination) - 2].text
    lastPage = 5 #TODO delete
    for index in range(1, int(lastPage)):
        link_page = urlFromMain + str(index) + filter_privato
        browser.get(link_page)
        print("## retrieving data from "+str(index)+" page")

        all_links_cards = browser.find_elements(By.CLASS_NAME, "BigCard-module_link__kVqPE")
        for index_cards in range(1, len(all_links_cards)):
            print("## retrieving data from card " + str(index_cards))
            linkForNewTab = all_links_cards[index_cards].get_attribute('href')
            url_list.append(linkForNewTab)
            try:
                scrapeFromNewTab(linkForNewTab)
            except NoSuchElementException:
                traceback.print_exc()
                linksNotFound.append(linkForNewTab)
                pass
    return Data_immobile(name,price,space, rooms, floor, description, title, url_list, number)

def scrapeFromNewTab(url):
    pin_tab = browser.window_handles[0]
    browser.execute_script('window.open("' + url + '");')
    browser.switch_to.window(browser.window_handles[1])

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
        print('--- Error occurred, no number for: '+str(title)+'; URL: '+str(url))
        pass

    name.append(name_scraped)
    price.append(price_scraped)
    space.append(space_scraped)
    rooms.append(rooms_scraped)
    floor.append(floor_scraped)
    description.append(description_scraped)
    title.append(title_scraped)
    number.append(number_scraped)
    bath.append(bath_scraped)

    browser.close()
    browser.switch_to.window(pin_tab)




