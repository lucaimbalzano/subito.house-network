import traceback
import time

import pywhatkit as pwk
from request import req_api_subito_message  as req

from settings import settings_message



def send_message(data_immobile_list_by_page):
    cont_msg = 0
    try:
                                        # 3 pages
        for index_page in range(0, len(data_immobile_list_by_page)):
                                            # 4 cards
            for index_house in range(0, len(data_immobile_list_by_page[index_page])):
                # numero = data_immobile_list[index_page].number[index_house] if data_immobile_list[index_page].number[index_house] else "NO NUMERO\n"

                req.post_api_subito(data_immobile_list_by_page[index_page][index_house])
                
                if data_immobile_list_by_page[index_page][index_house] != 0:
                    msg_from_settings_message = settings_message.MSG_INTRO_RENT_01 + data_immobile_list_by_page[index_page].url[index_house] + settings_message.MSG_PROPOSAL_RENT_01 + settings_message.PDR_EXAMPLE + settings_message.MSG_TIME_APPOINTMENT_02
                    pwk.sendwhatmsg_instantly(settings_message.PREFIX_ITA + data_immobile_list_by_page[index_page].number[index_house], msg_from_settings_message , tab_close=True)
                    time.sleep(2)
                    cont_msg+=1
                    print("[DEBUG] Message sent ["+ str(cont_msg)+"]")
    
    except Exception as e: 
        traceback.print_exc()
        print("Error in sending the message, "+str(e))
    

    