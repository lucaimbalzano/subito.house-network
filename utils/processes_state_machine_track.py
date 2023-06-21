# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



import datetime
import service.request.req_api_time_manager as tmanager_requests
import service.request.req_api_track as track_requests
import service.request.req_api_state as machine_requests
from service.request.dto.track_process_dto import TrackProcessRequestDTO as TrackProcess
from service.request.dto.time_manager_request_dto import TimeManagerRequestDto as TimeManager
from service.request.dto.machine_process_dto import MachineProcessRequestDTO as Machine, states
from service.response.res_api_state import get_state_object_from_json
from service.response.res_api_track import get_track_object_from_json


#TIME_MANAGER
def init_time_manager_default():
    current_date = f'{datetime.datetime.now():%Y-%m-%d}'
    current_date_time = f'{datetime.datetime.now():%H:%M:%S}'
    return TimeManager(None, 'NEVER-STOP', '5', 0, current_date, current_date_time, None, None)



#MACHINE
def init_machine_default():
    current_date = f'{datetime.datetime.now():%Y-%m-%d}'
    current_date_time = f'{datetime.datetime.now():%H:%M:%S}'
    return Machine(None, states.PLAY.name ,current_date, current_date_time, None, None, init_time_manager_default())



#PROCESS_TRACK
def init_track_process():
    # def __init__(self, idProcess, numPage, numCard, urlLastPage, urlLastCard, options, machine, errorStack):
    return TrackProcess(None,0,0, 'url','url','NO OPTIONS', 'NO ERROR',init_machine_default())






def update_track_process_by_new_one(seconds_exec, minutes_exec, current_values_track_process):
    current_values_track_process = get_track_object_from_json(current_values_track_process)
    current_date_time = f'{datetime.datetime.now():%Y-%m-%dT%H:%M:%SZ}'
    current_values_track_process.dateFinished = current_date_time
    current_values_track_process.seconds_execution = seconds_exec
    current_values_track_process.minutes_execution = minutes_exec

    track_requests.update_track_process(current_values_track_process)
    return current_values_track_process


def update_stop_state_by_trackProcessId(current_state_machine):
    current_state_machine = get_state_object_from_json(current_state_machine)
    current_state_machine.state = "STOP"
    machine_requests.update_state_machine_process(current_state_machine)

def get_active_state_by_trackProcessId(id_track_process):
    return Machine(None,"ACTIVE",id_track_process)


def init_state_machine_track_process():
    init_machine_default()
    track_process = init_track_process()

    # insert all init values for states process
    tmanager_requests.insert_time_manager(track_process.machine.timeManager)
    id_last_timeManager = tmanager_requests.get_id_of_last_time_manager()
    track_process.machine.timeManager = id_last_timeManager
    
    machine_requests.insert_state_machine_process(track_process.machine)
    id_last_machine = machine_requests.get_id_of_last_state_machine_process()
    track_process.machine = id_last_machine

    track_requests.insert_track_process(track_process)
    print('[DEBUG] TRACK PROCESS INITIALIZED - STATE MACHINE PROCESS INITIALIZED')

def finish_state_machine_track(seconds_exec, minutes_exec):
    id_last_track = track_requests.get_id_of_last_track_process()
    track_proc = track_requests.get_track_process_by_id(id_last_track)
    id_last_state_machine = machine_requests.get_id_of_last_state_machine_process()
    state_machine_proc = machine_requests.get_state_machine_process_by_id(id_last_state_machine)

    update_track_process_by_new_one(seconds_exec, minutes_exec, track_proc)
    update_stop_state_by_trackProcessId(state_machine_proc)
    print('[DEBUG] TRACK PROCESS ENDED - STATE MACHINE PROCESS ENDED')
