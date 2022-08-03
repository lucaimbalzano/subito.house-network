# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('C:/Users/lucai/Documents/Utils/SW/WebDriver/103/chromedriver.exe')
browser.get('https://areariservata.subito.it/login_form?login_tooltip=true')
filter_privato = '&advt=0'

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



def scrapingFromUrl(url):

    browser.get(url+str(0)+filter_privato)
    #DACANCELLARE
    time.sleep(4)
    privacy_alert = browser.find_element(By.ID, 'didomi-notice-agree-button')
    if privacy_alert != None:
        browser.execute_script("arguments[0].click();", privacy_alert)

    pagination = browser.find_elements(By.CLASS_NAME, "index-module_button-text__VZcja")
    lastPage = pagination[len(pagination) - 2].text
    time.sleep(5)
    for index in range(1, int(lastPage)):
        link_page = url + str(index) + filter_privato
        print("## retrieving data from first page")
        all_links_cards = browser.find_elements(By.CLASS_NAME, "BigCard-module_link__kVqPE")
        linkForNewTab = all_links_cards[index].get_attribute('href')
        scrapeFromNewTab(linkForNewTab)


def scrapeFromNewTab(url):
    pin_tab = browser.window_handles[0]
    browser.execute_script('window.open("' + url + '");')
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    title = browser.find_element(By.CLASS_NAME, "AdInfo_ad-info__title__7jXnY")
    price = browser.find_element(By.CLASS_NAME, "index-module_large__SUacX").text
    name = browser.find_element(By.CLASS_NAME, "index-module_name__hRS5a").text
    space_rooms_floor = browser.find_elements(By.CLASS_NAME, "MainData_label__4od4v")
    space = space_rooms_floor[0].text
    rooms = space_rooms_floor[1].text
    floor = space_rooms_floor[2].text
    description = browser.find_element(By.CLASS_NAME, "index-module_preserve-new-lines__ZOcGy").text

    try:
        all_buttons_new_tab = browser.find_elements(By.CLASS_NAME, "index-module_icon-only__gkRU8")
        chiama_btn = [btn for btn in all_buttons_new_tab if btn.text == "Chiama"]
        if len(chiama_btn) > 0:
            chiama_btn[0].click()
    except NoSuchElementException:
        print('--- Error occurred, no number for: '+title+'; URL: '+url)
        pass
    browser.close()
    time.sleep(1)
    browser.switch_to.window(pin_tab)




