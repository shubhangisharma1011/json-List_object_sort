import json
from urllib.request import urlopen


L=[]
url = "https://wegfinder.at/api/v1/stations"
response = urlopen(url)
data_json = json.loads(response.read())
for lisobjtodict in data_json:
    addurl = "https://api.i-mobility.at/routing/api/v1/nearby_address?latitude="+str(lisobjtodict['latitude'])+"&longitude="+str(lisobjtodict['longitude'])
    response1 = urlopen(addurl)
    data_json1 = json.loads(response1.read())
    if lisobjtodict['free_bikes'] != 0:
        lisobjtodict['address'] = data_json1['data']['name']
        L.append(lisobjtodict)

def sortbyname(obj):
    return obj['name']

def sortbybike(obj):
    return obj['free_bikes']
L.sort(key=sortbyname)
L.sort(key=sortbybike, reverse=True)
data = json.dumps(L, indent=4)
print(data)

