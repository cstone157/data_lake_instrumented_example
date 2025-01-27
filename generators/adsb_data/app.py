import requests

headers = {
#    'api-auth': "your uuid"
    'accept' : 'application/json'
}

#response = requests.get('https://adsbexchange.com/api/aircraft/lat/34.0549/lon/118.2426/dist/50/', headers = headers)
response = requests.get('https://api.adsb.lol/v2/lat/34.05/lon/-118.25/dist/200', headers = headers).json()
#data = response.text
air_craft = response["ac"]

print(len(air_craft))