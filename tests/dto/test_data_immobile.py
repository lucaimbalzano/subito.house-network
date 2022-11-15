



import random
from data_immobile import Data_immobile
from request.dto.house_request_dto import HouseRequestDTO


def get_fake_data_immobile():
      url_list = ['XQ', 'XY']  
      return Data_immobile("name","100","4", "4", "4", "description", "title", url_list , "3338902347")

def getHouseListPageTest(adv):
      houseListPage = []
      houseList = []
      for j in range(0,10):
            for i in range(0,30):
                  number_scraped = str(random.randrange(999, 999999))
                  houseList.append(HouseRequestDTO('name','price'+str(i),'space'+str(i),'rooms'+str(i),'floor','description','title','https://url_'+str(i),'NUMBER'+str(i)+number_scraped, False , adv, 'bathrooms', 'parking', 'energyClass', 'energyHeating', 'urlUserProfile', 'MILANO (MI)'))
            
            
            houseListPage.append(houseList)
            houseList = []
      return houseListPage
            
