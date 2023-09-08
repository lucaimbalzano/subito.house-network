# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from json import JSONEncoder
from typing import Any


class HouseRequestDTO:
  def __init__(self,idHouse, title, location, number, price,space,rooms,bathrooms,floor,totFloors,description, parking, contract, typology, energyClass, energyHeating, energyUnit , urlUserProfile, nameUser, otherCharacteristics, condominiumExpenses, caution, statusApartment, url, refDataAnnuncio,  vetrina, advertising, dateAdded, dateTimeAdded):
    self.idHouse = idHouse
    self.title = title
    self.location = location
    self.number = number
    self.price = price
    self.space = space
    self.rooms = rooms
    self.bathrooms = bathrooms
    self.floor = floor
    self.totFloor = totFloors
    self.description = description
    self.parking = parking
    self.contract = contract
    self.typology = typology
    self.energyClass = energyClass
    self.energyHeating = energyHeating
    self.energyUnit = energyUnit
    self.urlUserProfile = urlUserProfile
    self.nameUser = nameUser
    self.otherCharacteristics = otherCharacteristics
    self.condominiumExpenses = condominiumExpenses
    self.caution = caution
    self.statusApartment = statusApartment
    self.url = url  
    self.refDataAnnuncio = refDataAnnuncio
    self.vetrina = vetrina
    self.advertising = advertising
    self.dateAdded = dateAdded
    self.dateTimeAdded = dateTimeAdded
    

  def __setattr__(self, idHouse: str, value: Any) -> None:
    super().__setattr__(idHouse, value)

    

  # subclass JSONEncoder
class HouseRequestDTOEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__