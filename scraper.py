# from bs4 import BeautifulSoup #easy to scrape web-page information
# import requests, time
# import datetime as dt
# from datetime import datetime
# import pandas as pd
# from auxiliary_functions import *
#
# def scraping_web_prices_day_by_day():
#     now = datetime.now()
#     date_time_print = now.strftime("%m/%d/%Y, %H:%M:%S")
#     print("### START - "+date_time_print+" - scraper.py ###")
#     data_frame = pd.DataFrame() #it needs to store datas retrived
#     t = []
#     for index in range(1, 25):
#         link1 = "https://www.subito.it/annunci-lombardia/affitto/appartamenti/milano/milano/?advt="
#         #link2 = "&ys=2022"
#         link_page = link1 + str(index)
#
#         source = requests.get(link_page).text
#         soupScraper = BeautifulSoup(source, "lxml")
#         list_apartments = soupScraper.find_all("div", class_ ="BigCard-module_container__v6Cib")
#         for visible_description in list_apartments:
#             title = visible_description.find("h2", class_="index-module_sbt-text-atom__ed5J9 index-module_token-h6__FGmXw size-normal index-module_weight-semibold__MWtJJ ItemTitle-module_item-title__VuKDo BigCard-module_card-title__Cgcnt").text.strip()
#             data = sistema_data_ora(visible_description.find("span",
#                                                              "index-module_sbt-text-atom__ed5J9 index-module_token-caption__TaQWv index-module_size-small__XFVFl index-module_weight-semibold__MWtJJ index-module_date__Fmf-4 index-module_with-spacer__UNkQz"))
#             if data != None:
#                 diff = pd.Timestamp.now() - data
#                 if diff > dt.timedelta(days=1):
#                     data_frame = pd.DataFrame(t)
#                     data_frame = data_frame[
#                         ["name,price"]]
#                     data_frame = data_frame.sort_values("Prezzo", ascending=True)
#                     print(data_frame)
#                     return data_frame
#
