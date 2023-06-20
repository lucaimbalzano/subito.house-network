# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


class TrackProcessRequestDTO:
  def __init__(self, identifierProcess, numPage, numCard, urlLastPage, urlLastCard, errorStack, options, machine):
    self.identifierProcess = identifierProcess
    self.numPage = numPage
    self.numCard = numCard
    self.urlLastPage = urlLastPage
    self.urlLastCard = urlLastCard
    self.options = options
    self.machine = machine
    self.errorStack = errorStack
    

  def __setattr__(self, identifierProcess, value: any) -> None:
    super().__setattr__(identifierProcess, value)