



import datetime
import service.request.req_api_track as track_requests
import service.request.req_api_state as state_requests
from service.request.dto.track_process_dto import TrackProcessRequestDTO as TrackProcess
from service.request.dto.time_manager_request_dto import TimeManagerRequestDto as TimeManager
from service.request.dto.machine_process_dto import MachineProcessRequestDTO as Machine, states
from service.response.res_api_state import get_state_object_from_json
from service.response.res_api_track import get_track_object_from_json


def init_manager_default():
    return TimeManager(None, 'NEVER-STOP', 'NEVER-STOP', 0)

def init_machine_default():
    current_date = f'{datetime.datetime.now():%Y-%m-%d}'
    current_date_time = f'{datetime.datetime.now():T%H:%M:%S}'
    return Machine(None, states.PLAY,current_date, current_date_time, None, None, init_manager_default())

def get_current_track_process():
    return TrackProcess(None,'','', '','', 'NO ERROR', 'NO OPTIONS',init_machine_default())

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
    state_requests.update_state_machine_process(current_state_machine)

def get_active_state_by_trackProcessId(id_track_process):
    return Machine(None,"ACTIVE",id_track_process)


def init_state_machine_track():
    init_machine_default()
    current_trackProcessRequestDTO = get_current_track_process()

    # insert all init values for states process
    
    track_requests.insert_track_process(current_trackProcessRequestDTO)
    id_current_track = track_requests.get_id_of_last_track_process()
    state_requests.insert_state_machine_process(get_active_state_by_trackProcessId(id_current_track))
    print('[DEBUG] TRACK PROCESS INITIALIZED - STATE MACHINE PROCESS INITIALIZED')

def finish_state_machine_track(seconds_exec, minutes_exec):
    id_last_track = track_requests.get_id_of_last_track_process()
    track_proc = track_requests.get_track_process_by_id(id_last_track)
    id_last_state_machine = state_requests.get_id_of_last_state_machine_process()
    state_machine_proc = state_requests.get_state_machine_process_by_id(id_last_state_machine)

    update_track_process_by_new_one(seconds_exec, minutes_exec, track_proc)
    update_stop_state_by_trackProcessId(state_machine_proc)
    print('[DEBUG] TRACK PROCESS ENDED - STATE MACHINE PROCESS ENDED')
