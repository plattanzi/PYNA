#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try: #This is a new line, you also need to indent the code below this line by 4 white spaces
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK] [0] ['addr'])
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:    #this is a new line
        print('Could not collect adapter information')  #print error msg


