from bs4 import BeautifulSoup #easy to scrape web-page information
import requests, time
import datetime as dt
from datetime import datetime
import pandas as pd
from auxiliary_functions import *

def scraping_web_prices_day_by_day():
    now = datetime.now()
    date_time_print = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("### START - "+date_time_print+" - scraper.py ###")
    data_frame = pd.DataFrame() #it needs to store datas retrived
    t = []
    for index in range(1, 25):
        link1 = "https://www.subito.it/annunci-lombardia/affitto/appartamenti/milano/milano/?advt="
        #link2 = "&ys=2022"
        link_page = link1 + str(index)

        source = requests.get(link_page).text
        soupScraper = BeautifulSoup(source, "lxml")
        list_apartments = soupScraper.find_all("div", class_ ="BigCard-module_container__v6Cib")
        for visible_description in list_apartments:
            title = visible_description.find("h2", class_="index-module_sbt-text-atom__ed5J9 index-module_token-h6__FGmXw size-normal index-module_weight-semibold__MWtJJ ItemTitle-module_item-title__VuKDo BigCard-module_card-title__Cgcnt").text.strip()
            data = sistema_data_ora(visible_description.find("span",
                                                             "index-module_sbt-text-atom__ed5J9 index-module_token-caption__TaQWv index-module_size-small__XFVFl index-module_weight-semibold__MWtJJ index-module_date__Fmf-4 index-module_with-spacer__UNkQz"))
            if data != None:
                diff = pd.Timestamp.now() - data
                if diff > dt.timedelta(days=1):
                    data_frame = pd.DataFrame(t)
                    data_frame = data_frame[
                        ["Data_upload", "Marca", "Modello", "Versione", "Luogo", "Provincia", "Immatricolazione", "Km",
                         "Carburante", "Classe_emissioni", "Prezzo", "Link"]]
                    data_frame = data_frame.sort_values("Prezzo", ascending=True)
                    print(data_frame)
                    return data_frame
                else:
                    link = visible_description.a["href"]
                    list_apartment_detail = soupScraper.find_all("div", class_="BigCard-module_additional-info__aPSXC index-module_container__uSw-h index-module_grid__H7L7V index-module_grid-columns-4__MZU0U")


                    mq = visible_description.find("p",
                                                     "index-module_sbt-text-atom__ed5J9 index-module_token-body__GXE1P index-module_size-small__XFVFl index-module_weight-book__WdOfA index-module_info__GDGgZ").text.strip()
                    rooms = visible_description.find("p",
                                                         "index-module_sbt-text-atom__ed5J9 index-module_token-body__GXE1P index-module_size-small__XFVFl index-module_weight-book__WdOfA index-module_info__GDGgZ").text.replace(
                        "(", "").replace(")", "")
                    floor = visible_description.find("p",
                                                        "index-module_sbt-text-atom__ed5J9 index-module_token-body__GXE1P index-module_size-small__XFVFl index-module_weight-book__WdOfA index-module_info__GDGgZ").text.strip()
                    bath = visible_description.find("p",
                                                        "index-module_sbt-text-atom__ed5J9 index-module_token-body__GXE1P index-module_size-small__XFVFl index-module_weight-book__WdOfA index-module_info__GDGgZ").text.strip()

                    prize = (
                    visible_description.find("p", class_="index-module_price__N7M2x price index-module_small__4SyUf").text.split(" ")[
                        0])
                    if u'\xa0' in prize:
                        prize = prize.split((u'\xa0'))[0]
                    int_prize = int(prize.split(".")[0] + prize.split(".")[1])
                    marca, modello, versione, km, immatricolazione, carburante, euro = details_grid(link)
                    check = [x == None for x in (marca, modello, versione, km, immatricolazione, carburante, euro)]
                    if False not in check:
                        continue
                    tmp = dict(Data_upload=data, Marca=marca, Modello=modello, Versione=versione, Luogo=luogo,
                               Provincia=provincia, Immatricolazione=immatricolazione, Km=km, Carburante=carburante,
                               Classe_emissioni=euro, Prezzo=int_prize, Link=link)
                    t.append(tmp)
