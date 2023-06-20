



import datetime
from service.request.dto.track_process_dto import TrackProcessRequestDTO



# TESTS in main 
# track_test = get_fake_track()
# # insert_track_process(track_test)
# id = get_id_of_last_track_process()
# response =  get_track_process_by_id(id)
# track_proc = get_track_object_from_json(response)
# track_proc.numCard = 100
# res = update_track_process(track_proc)



def get_fake_track():
    # YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]
    # output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    output_date = f'{datetime.datetime.now():%Y-%m-%dT%H:%M:%SZ}'
    return TrackProcessRequestDTO(None,10,20,'NO ERROR', output_date,None,'','','')