# Dreams without Goals are just Dreams



import json
from request.dto.state_machine_process_dto import StateMachineProcessRequestDTO
from types import SimpleNamespace


def get_state_object_from_json(json_state_process):
    simpleNamespace_state_machine_process = json.loads(json_state_process, object_hook=lambda d : SimpleNamespace(**d))
    return(StateMachineProcessRequestDTO(
        simpleNamespace_state_machine_process.id_state_machine,
        simpleNamespace_state_machine_process.state,
        simpleNamespace_state_machine_process.processId
    ))