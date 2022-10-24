# coding=utf-8

from email import *
from browser.browser import Browser
from messages import send_message_by_data_house
from scraper.scraper_selenium import *
from utils.auxiliary_functions_excel import writeExcelByDataImmobile
from utils.cronometer import ChronoMeter
from utils.auxiliary_functions import *
from settings import settings
import json
import traceback
import datetime as dt
import time
# import pandas as pd


def getDataImmobile(link):
    data_immobile = scrapingFromUrl(link)
    return data_immobile

if __name__ == '__main__':
    chrono = ChronoMeter()
    chrono.start_chrono()

    # while True:
    browser = Browser.get_browser()
    login(browser)
    try:
        data_immobile_pages = scrollByPage(browser)
        # url_list = ['url_test', 'XY']  
        # data_immobile = Data_immobile("name","100","4", "4", "4", "description", "title", url_list , "348 604 9869")
        if data_immobile_pages is not None:
            # writeExcelByDataImmobile(data_immobile)
            # write on DB send_message(data_immobile)
            send_message_by_data_house.send_message(data_immobile_pages)
        else:
            print("Error Occurred: No data retrived")
            quit()
    except Exception:
        traceback.print_exc()
    chrono.stop_chrono()
    chrono.print_time()
    exit(1)


        # sent_working_email()
        # try:
        #     sent_working_email()
        # except Exception as e:
        #     print(e)
        #     # send_wrong_email()
        # todayMinSec = dt.datetime.today()
        # tomorrow = todayMinSec + dt.timedelta(days=1)
        # tomorrowMinSec = tomorrow.combine(tomorrow, dt.time(20, 45))
        # differenceTodayTomorrow = tomorrowMinSec - dt.datetime.today()
        # totalSecondsDifferenceTodayTomorrow = differenceTodayTomorrow.total_seconds()
        # print("difference to understand::::", dt.datetime.today() + dt.timedelta(seconds=totalSecondsDifferenceTodayTomorrow))
        # time.sleep(totalSecondsDifferenceTodayTomorrow)
