# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
from enum import Enum

class MachineProcessRequestDTO:
  def __init__(self, idStatMachine, state, startedDate, startedDateTime, finishDate, finishDateTime, timeManger):
    self.idStatMachine = idStatMachine
    self.state = states
    self.startedDate = startedDate
    self.startedDateTime = startedDateTime
    self.finishDate = finishDate
    self.finishDateTime = finishDateTime
    self.timeManger = timeManger
    
  def __setattr__(self, id_state_machine, value: any) -> None:
    super().__setattr__(id_state_machine, value)



states = Enum('state', ['PLAY', 'PAUSE', 'STOP'])
  