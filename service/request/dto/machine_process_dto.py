# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
from json import JSONEncoder
from enum import Enum

from service.request.dto.time_manager_request_dto import TimeManagerRequestDto as TimeManager

class MachineProcessRequestDTO:
    def __init__(self, idStateMachine, state, startedDate, startedDateTime, finishDate, finishDateTime, timeManager):
        self.idStateMachine = idStateMachine
        self.state = state
        self.startedDate = startedDate
        self.startedDateTime = startedDateTime
        self.finishDate = finishDate
        self.finishDateTime = finishDateTime
        self.timeManager = timeManager
    
class MachineProcessRequestDTOEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (MachineProcessRequestDTO, TimeManager)):
            return o.__dict__
        if isinstance(o, (Enum, states)):
            return o.value
        return super().default(o)

states = Enum('state', ['PLAY', 'PAUSE', 'STOP'])
