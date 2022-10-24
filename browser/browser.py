from selenium import webdriver
from settings import settings



def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito");
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options



class Browser:

    def get_browser():
        options = get_options()
        browser = webdriver.Chrome(settings.PATH_CHROME_DRIVER, chrome_options=options)
        return browser