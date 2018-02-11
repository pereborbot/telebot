import json
import time
import datetime
import re
from pprint import pprint

json_data = json.load(open('output.json'))

#pprint (json_data)

#print('#############')

#pprint (json_data['ok'])

#print('#############')

#pprint (json_data['result'])


print('Starting...')


#for x in range(0,len(json_data['result'])):
#    first_name = json_data['result'][x]['message']['from']['first_name']
#    #if (first_name == "O"):
#    if re.search(r'.*J.*', first_name):
#        pprint (json_data['result'][x])
#    else:
#        print ("Not in", first_name)
#
#print('#############')
#
#str = 'loooog'
#if re.search(r'too', str):
#    print (str) 
#else:
#    print ("Nothing")

def print_now():
    print (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))

print_now()

weekNumber = datetime.date.today().isocalendar()[1]
print ('Week number:', weekNumber)


def get_watchman():
#    print (weekNumber % 2)
    if ((weekNumber % 2) == 0):
#        print('hello')
        watchman = "O"
        reservist = "john"
    else:
        watchman = "john"
        reservist = "O"
    return (watchman, reservist)
#get_watchman()

watchman, reservist = (get_watchman())

print(watchman)
print(reservist)








