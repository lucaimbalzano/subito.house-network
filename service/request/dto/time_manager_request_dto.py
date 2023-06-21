# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


class TimeManagerRequestDto:
  def __init__(self, idTimeManager, workAgentState, cycleAgent, numberCycle, addedDate, addedDateTime, updateDate, updateDateTime):
    self.idTimeManager = idTimeManager
    self.workAgentState = workAgentState
    self.cycleAgent = cycleAgent
    self.numberCycle = numberCycle
    self.addedDate =addedDate 
    self.addedDateTime = addedDateTime
    self.updateDate = updateDate
    self.updateDateTime = updateDateTime

  def __setattr__(self, idTimeManager, value: any) -> None:
    super().__setattr__(idTimeManager, value)