# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


import random
from request.dto.house_request_dto import HouseRequestDTO



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
            
