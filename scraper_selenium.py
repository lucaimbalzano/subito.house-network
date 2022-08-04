# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import time
from data_immobile import Data_immobile
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('C:/Users/lucai/Documents/Utils/SW/WebDriver/103/chromedriver.exe')
browser.get('https://areariservata.subito.it/login_form?login_tooltip=true')
filter_privato = '&advt=0'
linkForNewTab = ''
name,price,space, rooms, floor, description, title, url_list, number =[],[],[],[],[],[],[],[],[]

def login():
    time.sleep(4)
    privacy_alert = browser.find_element(By.ID, 'didomi-notice-agree-button')
    if privacy_alert != None:
        browser.execute_script("arguments[0].click();", privacy_alert)
        # continue_without_accept = browser.find_elements(By.CLASS_NAME, "didomi-continue-without-agreeing")
        # browser.execute_script("arguments[0].click();", continue_without_accept)

    username = browser.find_element("xpath","//input[@name='username']")
    password = browser.find_element("xpath","//input[@name='password']")
    username.send_keys('lucaimbalzano@gmail.com')
    password.send_keys('Slowspoke00')
    time.sleep(2)
    submit = browser.find_element("xpath","//button[@type='submit']").click()
    time.sleep(5)



def scrapingFromUrl(urlFromMain):
    browser.get(urlFromMain+str(0)+filter_privato)

    pagination = browser.find_elements(By.CLASS_NAME, "index-module_button-text__VZcja")
    lastPage = pagination[len(pagination) - 2].text
    time.sleep(3)

    for index in range(1, int(lastPage)):
        link_page = urlFromMain + str(index) + filter_privato
        print("## retrieving data from "+str(index)+" page")

        all_links_cards = browser.find_elements(By.CLASS_NAME, "BigCard-module_link__kVqPE")
        linkForNewTab = all_links_cards[index].get_attribute('href')
        url_list.append(linkForNewTab)
        scrapeFromNewTab(linkForNewTab)
        d = Data_immobile(name,price,space, rooms, floor, description, title, url_list, number)
        d.print()
    return Data_immobile(name,price,space, rooms, floor, description, title, url_list, number)

def scrapeFromNewTab(url):
    pin_tab = browser.window_handles[0]
    browser.execute_script('window.open("' + url + '");')
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    title_scraped = browser.find_element(By.CLASS_NAME, "AdInfo_ad-info__title__7jXnY").text
    price_scraped = browser.find_element(By.CLASS_NAME, "index-module_large__SUacX").text
    name_scraped = browser.find_element(By.CLASS_NAME, "index-module_name__hRS5a").text
    space_rooms_floor = browser.find_elements(By.CLASS_NAME, "MainData_label__4od4v")
    space_scraped = space_rooms_floor[0].text
    number_scraped = ''
    floor_scraped = ''
    rooms_scraped = ''
    if(len(space_rooms_floor) > 1):
        rooms_scraped = space_rooms_floor[1].text
        if( "agn" in space_rooms_floor[2].text):
            bath_scraped = space_rooms_floor[2].text
        else:
            floor_scraped = space_rooms_floor[2].text
    description_scraped = browser.find_element(By.CLASS_NAME, "index-module_preserve-new-lines__ZOcGy").text


    try:
        all_buttons_new_tab = browser.find_elements(By.CLASS_NAME, "index-module_icon-only__gkRU8")
        chiama_btn = [btn for btn in all_buttons_new_tab if btn.text == "Contatta"]
        index = all_buttons_new_tab.index(chiama_btn[1])

        if len(chiama_btn) > 0 and int(index) == 6 :
            all_buttons_new_tab[int(index)-1].click()
            time.sleep(3)
            number_scraped = browser.find_elements(By.CLASS_NAME, "index-module_isVisible__GstjN")[0].text
            number_scraped_editing = number_scraped.replace("Numero di telefono", "")
            number_scraped = number_scraped_editing.replace("\n", "")
            index = 0


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

    browser.close()
    time.sleep(1)
    browser.switch_to.window(pin_tab)




