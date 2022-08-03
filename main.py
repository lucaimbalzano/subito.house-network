# coding=utf-8
from messages_and_email import *
from scraper_selenium import *

if __name__ == '__main__':
    while True:
        print("## started cycle - inside loop ##")
        ora = dt.datetime.now().time().hour
        minuti = dt.datetime.now().time().minute
        scrapingFromUrl("");
        sent_working_email()
        try:
            sent_working_email()
        except Exception as e:
            print(e)
            # send_wrong_email()
        todayMinSec = dt.datetime.today()
        tomorrow = todayMinSec + dt.timedelta(days=1)
        tomorrowMinSec = tomorrow.combine(tomorrow, dt.time(20, 45))
        differenceTodayTomorrow = tomorrowMinSec - dt.datetime.today()
        totalSecondsDifferenceTodayTomorrow = differenceTodayTomorrow.total_seconds()
        print("difference to understand::::", dt.datetime.today() + dt.timedelta(seconds=totalSecondsDifferenceTodayTomorrow))
        time.sleep(totalSecondsDifferenceTodayTomorrow)
