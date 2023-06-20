# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def exception_NoSuchElementExeption_house_ByFieldFinder(browser,byFieldFinder,class_name, neededTextOutput):
    field_house = None
    try:
            if neededTextOutput:
                field_house = browser.find_element(byFieldFinder, class_name).text
            else:
                field_house = browser.find_element(byFieldFinder, class_name)

    except NoSuchElementException as nse:
        print("------ error occurred: "+nse)
        pass
    finally:
        return field_house


def exception_NoSuchElementExeption_house_ByFieldFinder_asList(browser,byFieldFinder,class_name, neededTextOutput):
    field_house = None
    try:
            if neededTextOutput:
                field_house = browser.find_elements(byFieldFinder, class_name)[0].text
            else:
                field_house = browser.find_elements(byFieldFinder, class_name)

    except NoSuchElementException as nse:
        print("------ error occurred: "+nse)
        pass
    return field_house


def exception_NoSuchElementExeption_house_ByFieldFinder_byGetAttribute(browser,byFieldFinder,class_name, getAttribute):
    field_house = None
    try:
            
        field_house = browser.find_element(byFieldFinder, class_name).get_attribute(getAttribute)

    except NoSuchElementException as nse:
        print("------ error occurred: "+nse)
        pass
    return field_house
