# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


class MessageRequestDTO:
  def __init__(self,messageId,dateSent,message,idHouseRequest, options):
    self.messageId = messageId
    self.dateSent = dateSent
    self.message = message
    self.idHouseRequest = idHouseRequest
    self.options = options

  def __setattr__(self, messageId, value: any) -> None:
    super().__setattr__(messageId, value)