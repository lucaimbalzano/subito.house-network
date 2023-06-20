# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


class TimeManagerRequestDto:
  def __init__(self, idTimeManager, workAgentState, cycleAgent, numberCycle):
    self.idTimeManager = idTimeManager,
    self.workAgentState = workAgentState,
    self.cycleAgent = cycleAgent,
    self.numberCycle = numberCycle

  def __setattr__(self, idTimeManager, value: any) -> None:
    super().__setattr__(idTimeManager, value)