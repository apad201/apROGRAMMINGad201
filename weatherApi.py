import requests

key = '72fa5852e40ed29a'
ApiUrl = 'http://api.wunderground.com/api/' + key + '/forecast/q/NC/Durham.json'

r = requests.get(ApiUrl)
forecast = r.txt
print forecast['forecast']['txt_forecast']['forecastday'][0]['fcttext']