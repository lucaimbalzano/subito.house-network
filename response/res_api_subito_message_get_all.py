from json import JSONEncoder, JSONDecoder
from request.dto.house_request_dto import HouseRequestDTO


class HousesListDTO:
  def __init__(self,houseRequestDTO:HouseRequestDTO, HouseRequestDTO):
        self.houseRequestDTO = houseRequestDTO
  

class HousesListDTOEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class HousesListDTODecoder(JSONDecoder):
        def default(self, o):
            return o.__dict__