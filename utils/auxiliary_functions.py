import datetime as dt
from bs4 import BeautifulSoup
# import pandas as pd
import openpyxl
import requests,re,time
from data_immobile import Data_immobile
from datetime import datetime
from openpyxl import Workbook



def sistema_data_ora(caricato_il):
    if caricato_il == None:
        return None
    if "Oggi" in caricato_il.text:
        index = (caricato_il.text.find(":"))
        ora = int(caricato_il.text[index - 2:index])
        minuti = int(caricato_il.text[index + 1:index + 3])
        orario = dt.time(ora, minuti)
        today = dt.date.today()
        data_con_orario = dt.datetime.combine(today, orario)
    elif "Ieri" in caricato_il.text:
        index = (caricato_il.text.find(":"))
        yesterday = dt.date.today() - dt.timedelta(days=1)
        ora = int(caricato_il.text[index - 2:index])
        minuti = int(caricato_il.text[index + 1:index + 3])
        orario = dt.time(ora, minuti)
        data_con_orario = dt.datetime.combine(yesterday, orario)
    else:
        mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
        split = caricato_il.text.split(" ")
        strorario = split[3]
        index = (strorario.find(":"))
        ora = int(strorario[index - 2:index])
        minuti = int(strorario[index + 1:index + 3])
        orario = dt.time(ora, minuti)
        giorno = int(split[0])
        mese = mesi.index(split[1]) + 1
        data = dt.date(2020, mese, giorno)
        data_con_orario = dt.datetime.combine(data, orario)
    return data_con_orario


def starting_time(hour, minute):
    if dt.datetime.now().hour != hour or dt.datetime.now().minute != minute:
        today = dt.datetime.today()
        domani = today + dt.timedelta(days=1)
        ora = dt.time(hour, minute)

        
        until = domani.combine(domani, ora)
        diff = until - dt.datetime.today()
        secnd = diff.total_seconds()
        print("i will start at:", dt.datetime.today() + dt.timedelta(seconds=secnd))
        time.sleep(secnd)