from typing import Any


class Data_immobile:
  def __init__(self,name,price,space,rooms,floor,description,title,url,number):
    self.name = name
    self.price = price
    self.space = space
    self.rooms = rooms
    self.floor = floor
    self.description = description
    self.title = title
    self.url = url
    self.number = number

  def __setattr__(self, name: str, value: Any) -> None:
    super().__setattr__(name, value)



