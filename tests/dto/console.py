# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



def input_console():
       
   advertising = ''
   message = True
   excel = True
   exit = False

   print(' ')
   while True: 
       print(' ')
       print(' enter the key ''exit'' to escape.. ')
       result_input =  input('Do you want to scrape Rent[1] or Sale[2] houses :'  )
       if result_input != '1' and result_input !='2' and result_input != 'exit':
           print('you didnt insert 1,2,exit..')
           print('you inserted: '+str(result_input))
       else:
           if result_input == 'exit':
                   exit = True
           elif result_input == '1':
               advertising = '1'
               break
           elif result_input == '2':
               advertising = '2'
               break
   print(' ')
   while True: 
       print(' ')
       print(' enter the key ''exit'' to escape.. ')
       boolResult =  input('Do you want to send whatsapp message [y/n]:  ')
       if boolResult != 'y' and boolResult != 'Y' and boolResult != 'n' and boolResult != 'N' and boolResult != 'exit':
           print('you didnt insert y,Y,n,N,exit..')
           print('you inserted: '+str(boolResult))
       else:
           if boolResult == 'y' or boolResult == 'Y':
               message = True
               break
           elif boolResult == 'n' or boolResult == 'N':
               message = False
               break
           elif boolResult == 'exit':
               exit = True
   
   while True: 
     print(' ')
     print(' enter the key ''exit'' to escape.. ')
     boolResult =  input('Do you want to write excel [y/n]:  ')
     if boolResult != 'y' and boolResult != 'Y' and boolResult != 'n' and boolResult != 'N' and boolResult != 'exit':
         print('you didnt insert y,Y,n,N,exit..')
         print('you inserted: '+str(boolResult))
     else:
         if boolResult == 'y' or boolResult == 'Y':
             excel = True
             break
         elif boolResult == 'n' or boolResult == 'N':
             excel = False
             break
         elif boolResult == 'exit':
             exit = True

   return Console(advertising,message,excel,exit)





class Console:
    def __init__(self,advertising, message,excel, exit):
        self.advertising = advertising
        self.message = message
        self.excel = excel
        self.exit = exit