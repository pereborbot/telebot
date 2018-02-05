import json
import re
from pprint import pprint

json_data = json.load(open('output.json'))

pprint (json_data)

print('#############')

pprint (json_data['ok'])

print('#############')

#pprint (json_data['result'])




for x in range(0,len(json_data['result'])):
    if ((json_data['result'][x]['message']['from']['first_name']) == "O"):
        pprint (json_data['result'][x])

print('#############')

str = 'loooog'
if re.search(r'too', str):
    print (str) 
else:
    print ("Nothing")
