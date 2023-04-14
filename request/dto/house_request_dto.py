# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from json import JSONEncoder
from typing import Any


class HouseRequestDTO:
  def __init__(self,name,price,space,rooms,floor,description,title,url,number, vetrina, advertising, bathrooms, parking, energyClass, energyHeating, urlUserProfile, location):
    self.name = name
    self.price = price
    self.space = space
    self.rooms = rooms
    self.floor = floor
    self.description = description
    self.title = title
    self.url = url
    self.number = number
    self.vetrina = vetrina
    self.advertising = advertising
    self.bathrooms = bathrooms
    self.parking = parking
    self.energyClass = energyClass
    self.energyHeating = energyHeating
    self.urlUserProfile = urlUserProfile
    self.location = location

  def __setattr__(self, name: str, value: Any) -> None:
    super().__setattr__(name, value)

    

  # subclass JSONEncoder
class HouseRequestDTOEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__