# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:/Users/lucai/Documents/Utils/SW/WebDriver/chromedriver.exe')
driver.get('https://www.subito.it/annunci-lombardia/affitto/appartamenti/milano/milano/?advt=0')
time.sleep(2)

def scrapingFromUrl(url):
    for index in range(1, 25):
        url = "";
        link1 = "https://www.subito.it/annunci-lombardia/affitto/appartamenti/milano/milano/?advt="
        # link2 = "&ys=2022"
        link_page = link1 + str(index)

        # all_href = driver.find_elements_by_tag_name("a")
        # connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
        # add_connection(connect_buttons)

        # div class ="pagination_pagination-button-wrapper__czWc4 unselected-page"