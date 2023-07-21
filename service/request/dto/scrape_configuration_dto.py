# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


from enum import Enum
from service.request.dto.machine_process_dto import MachineProcessRequestDTO as Machine
from service.request.dto.time_manager_request_dto import TimeManagerRequestDto as TimeManager
from json import JSONEncoder


class FlowInputScraperConfigRequestDTO(models.Model):
    self.id_flow_input_scraper_config = models.AutoField(primary_key=True)
    self.totNumPage = models.CharField(max_length=4)
    self.self.totNumCards = models.CharField(max_length=4)
    self.contract = models.CharField(max_length=10)
    self.url = models.CharField(max_length=300)
    self.username = models.CharField(max_length=30)
    self.password = models.CharField(max_length=30)
    self.refreshSearch = JSONField()
    self.message = models.BooleanField()
    self.messageWebSite = models.BooleanField()





class FlowInputScrapeConfigurationRequestDTO:
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