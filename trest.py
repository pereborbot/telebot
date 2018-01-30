import json
from pprint import pprint

json_data = json.load(open('output.json'))

pprint (json_data)

print('#############')

pprint (json_data['ok'])

print('#############')

pprint (json_data['result'])


for x in (json_data['result']):
    pprint json_data['result'][x])

