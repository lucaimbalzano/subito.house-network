# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


from selenium import webdriver
from settings import settings

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito");
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options



class Browser:

    def get_browser():
        options = get_options()
        # browser = webdriver.Chrome(executable_path=settings.PATH_CHROME_DRIVER, chrome_options=options)
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return browser
