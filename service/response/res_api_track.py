# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from json import JSONEncoder, JSONDecoder
import json
from service.request.dto.track_process_dto import TrackProcessRequestDTO
from types import SimpleNamespace




class TrackProcessListDTO:
  def __init__(self,trackProcessDTO:TrackProcessRequestDTO):
        self.trackProcessDTO = trackProcessDTO
  

class TrackProcessListDTOEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class TrackProcessListDTODecoder(JSONDecoder):
        def default(self, o):
            return o.__dict__

def get_track_object_from_json(json_track_process):
    simpleNamespace_track_process = json.loads(json_track_process, object_hook=lambda d : SimpleNamespace(**d))
    return(TrackProcessRequestDTO(
        simpleNamespace_track_process.identifierProcess,
        simpleNamespace_track_process.numPage,
        simpleNamespace_track_process.numCard,
        simpleNamespace_track_process.errorStack,
        simpleNamespace_track_process.dateStarted,
        simpleNamespace_track_process.dateFinished,
        simpleNamespace_track_process.options,
        simpleNamespace_track_process.seconds_execution,
        simpleNamespace_track_process.minutes_execution
    ))