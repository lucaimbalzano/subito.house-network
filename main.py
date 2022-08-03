# coding=utf-8
import json

from messages_and_email import *
from scraper_selenium import *
import pandas as pd


link = 'https://www.subito.it/annunci-lombardia/affitto/appartamenti/milano/milano/?o='

if __name__ == '__main__':

    while True:
        print("## started cycle - inside loop ##")
        ora = dt.datetime.now().time().hour
        minuti = dt.datetime.now().time().minute
        #login()
        data_immobile = scrapingFromUrl(link)
        writeExcelByDataImmobile(data_immobile)

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
