


def yn_console(field_yn,field_name):
    while True: 
        print(' enter the key ''exit'' to escape.. ')
        boolResult =  input('Do you want to send '+field_name+' [y/n]')
        if boolResult != 'y' or field_yn != 'Y' or boolResult != 'n' or field_yn != 'N' or field_yn != 'exit':
            print('you didnt insert y,Y,n,N,exit..')
            print('you inserted: '+str(field_yn))
        else:
            if boolResult != 'y' or field_yn != 'Y':
                field_yn = True
            elif boolResult != 'n' or field_yn != 'N':
                field_yn = False
            elif boolResult == 'exit':
                return True


def input_console():
   
   advertising = ''
   message = True
   excel = True
   exit = False

   while True: 
    print(' enter the key ''exit'' to escape.. ')
    advertising =  input('Do you want to scrape Rent[1] or Sale houses[2]')
    if advertising != 1 or advertising !=2 or advertising != 'exit':
        print('you didnt insert 1,2,exit..')
        print('you inserted: '+str(advertising))
    else:
        if advertising == 'exit':
                exit = True
        break
    
    if yn_console(message,'whatsapp message'):
        exit = True
    if yn_console(excel,'excel'):
        exit = True

    return Console(advertising,message,excel,exit)





class Console:
    def __init__(self,advertising, message,excel, exit):
        self.advertising = advertising
        self.message = message
        self.excel = excel
        self.exit = exit