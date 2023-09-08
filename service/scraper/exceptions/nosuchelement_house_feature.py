# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from settings.settings_subito_find_element import SUBITO_DETTAGLI_HOUSE_XPATH


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


def exception_NoSuchElementException_price_house_width_window_dispose_different_DOM(browser,byFieldFinder, xpath_min_width, xpath_max_width):
    price_scraped = None
    try:
            
        price_scraped = browser.find_element(byFieldFinder, xpath_min_width).text

    except Exception as e:
        print("------ error occurred while scraping price (min-width-window): "+e)
        pass

    finally:
        if price_scraped is None:
            try:
                price_scraped = browser.find_element(byFieldFinder, xpath_max_width).text
            except Exception as e:
                print("------ error occurred while scraping price (max-width-window): "+e)
                pass
            finally:
                if price_scraped is None:
                    return 'NOT SPECIFIED'
                else:
                    return price_scraped 
        else:
            return price_scraped

def excepion_NoSuchElementException_dettagli_house(browser, byFieldFinder, xpath_string):
    dettagli_scraped = None
    
    try:
            
        dettagli_scraped = browser.find_element(byFieldFinder, xpath_string).text.split('\n')
        dettagli_scraped = '; '.join(dettagli_scraped)

    except Exception as e:
        print("------ error occurred by scraping dettagli house: "+e)
        pass

    finally:
        if dettagli_scraped is None:
            return 'NOT SPECIFIED'
        return dettagli_scraped

def excepion_NoSuchElementException_riscaldamento_house(browser, byFieldFinder, xpath_string):
    riscaldamento_scraped = None
    
    try:
            
        riscaldamento_scraped = browser.find_element(byFieldFinder, xpath_string).text.split('\n')
        
    except Exception as e:
        print("------ error occurred by scraping riscaldamento house: "+e)
        pass

    finally:
        if riscaldamento_scraped is None:
            return 'NOT SPECIFIED'
        return riscaldamento_scraped

def excepion_NoSuchElementException_caratteristiche_house(browser, byFieldFinder, xpath_string):
    caratteristiche_scraped = None
    
    try:
            
        caratteristiche_scraped = browser.find_element(byFieldFinder, xpath_string).text.split('\n')
        
    except Exception as e:
        print("------ error occurred by scraping caratteristiche house: "+e)
        pass

    finally:
        if caratteristiche_scraped is None:
            return 'NOT SPECIFIED'
        return caratteristiche_scraped