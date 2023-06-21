# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


from enum import Enum
from service.request.dto.machine_process_dto import MachineProcessRequestDTO as Machine
from service.request.dto.time_manager_request_dto import TimeManagerRequestDto as TimeManager
from json import JSONEncoder

class TrackProcessRequestDTO:
    def __init__(self, idProcess, numPage, numCard, urlLastPage, urlLastCard, options, errorStack, machine):
        self.idProcess = idProcess
        self.numPage = numPage
        self.numCard = numCard
        self.urlLastPage = urlLastPage
        self.urlLastCard = urlLastCard
        self.options = options
        self.errorStack = errorStack
        self.machine = machine
        

class TrackProcessRequestDTOEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (TrackProcessRequestDTO, Machine, TimeManager)):
            return o.__dict__
        if isinstance(o, Enum):
            return o.value
        return super().default(o)