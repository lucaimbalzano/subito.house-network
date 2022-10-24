# coding=utf-8

from email import *
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

    while True:
        for i in (1, 10):
            print("## started cycle - inside loop ##")
            login()
            try:
                data_immobile = scrapingFromUrl(settings.BASE_LINK_RENT_HOUSE)
                if(data_immobile != None):
                    writeExcelByDataImmobile(data_immobile)
                else:
                    print("Error Occurred: No data retrived")
            except Exception:
                traceback.print_exc()
        chrono.stop_chrono()
        chrono.print_time()
        print("## finished cycle - exit ##")
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
