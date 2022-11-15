




class MessageRequestDTO:
  def __init__(self,messageName,dateAdded,message,numberSent):
    self.messageName = messageName
    self.dateAdded = dateAdded
    self.message = message
    self.numberSent = numberSent

  def __setattr__(self, messageName, value: any) -> None:
    super().__setattr__(messageName, value)