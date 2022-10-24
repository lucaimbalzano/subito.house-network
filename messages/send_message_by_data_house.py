import traceback
import pywhatkit as pwk
import keyboard
from settings import settings_message



def send_message(data_immobile_list):
    # using Exception Handling to avoid unexpected errors
    try:
    # sending message in Whatsapp in India so using Indian dial code (+91)
        # pwk.sendwhatmsg(settings_message.PREFIX_ITA + house.number, "This is a test")
        for index_page in range(0, len(data_immobile_list)):
            for index_house in range(0, len(data_immobile_list[index_page].name[0])):
                numero = data_immobile_list[index_page].number[index_house] if data_immobile_list[index_page].number[index_house] else "NO NUMERO\n"
                # return Data_immobile(nameList,priceList,spaceList, roomsList, floorList, descriptionList, titleList, urlHouseDetailList, numberList)
                msg_from_settings_message = settings_message.MSG_INTRO_RENT_01 + data_immobile_list[index_page].url[index_house] + settings_message.MSG_PROPOSAL_RENT_01 + settings_message.PDR_EXAMPLE + settings_message.MSG_TIME_APPOINTMENT_01
                stringa_test = data_immobile_list[index_page].title[index_house] + "\n" + "numero in teoria sarebbe: " + numero+"\n" + msg_from_settings_message
                
                pwk.sendwhatmsg_instantly(settings_message.PREFIX_ITA + "348 604 9869", stringa_test,tab_close=True)
                # if index_house !=0:
                #     keyboard.press_and_release('ctrl+w')
                print("Message sent ["+ str(index_house)+"]")
    
        # error message
    except Exception as e: 
        traceback.print_exc()
        print("Error in sending the message, "+str(e))
    # finally:
    #     keyboard.press_and_release('ctrl+w')