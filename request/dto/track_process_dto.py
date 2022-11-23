# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


class TrackProcessRequestDTO:
  def __init__(self, identifierProcess, numPage, numCard, errorStack, dateStarted, dateFinished, options, seconds_execution, minutes_execution):
    self.identifierProcess = identifierProcess
    self.numPage = numPage
    self.numCard = numCard
    self.errorStack = errorStack
    self.dateStarted = dateStarted
    self.dateFinished = dateFinished
    self.options = options
    self.seconds_execution = seconds_execution
    self.minutes_execution = minutes_execution

  def __setattr__(self, identifierProcess, value: any) -> None:
    super().__setattr__(identifierProcess, value)