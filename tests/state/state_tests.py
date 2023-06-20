



from service.request.dto.machine_process_dto import MachineProcessRequestDTO



# TESTS in main for MachineProcessRequestDTO
# state_test = get_fake_state_machine()
# res_post = insert_state_machine_process(state_test)
# id_last_state = get_id_of_last_state_machine_process()
# res_get_by_id = get_state_machine_process_by_id(id_last_state)
# res_get_by_id = get_state_object_from_json(res_get_by_id)
# res_get_by_id.state = 'STOP'
# res_update = update_state_machine_process()


def get_fake_state_machine():
    #  id_state_machine, state, processId):?
    return MachineProcessRequestDTO(None,'ACTIVE',3)