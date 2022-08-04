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

  def print(self):
        print("= OBJECT =")
        print("name: ", self.name)
        print("price: ", self.price)
        print("space: ", self.space)
        print("rooms: ", self.rooms)
        print("floor: ", self.floor)
        print("desc: ", self.description)
        print("title: ", self.title)
        print("url: ", self.url)
        print("number: ", self.number)
        print(" ")




