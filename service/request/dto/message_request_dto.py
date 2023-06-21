# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


class MessageRequestDTO:
  def __init__(self,messageId,dateSent,dateTimeSent,message,house, options):
    self.messageId = messageId
    self.dateSent = dateSent
    self.dateTimeSent = dateTimeSent
    self.message = message
    self.house = house
    self.options = options

  def __setattr__(self, messageId, value: any) -> None:
    super().__setattr__(messageId, value)