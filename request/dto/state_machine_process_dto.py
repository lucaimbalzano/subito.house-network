# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


class StateMachineProcessRequestDTO:
  def __init__(self, id_state_machine, state, processId):
    self.id_state_machine = id_state_machine
    self.state = state
    self.processId = processId

  def __setattr__(self, id_state_machine, value: any) -> None:
    super().__setattr__(id_state_machine, value)