import requests as rq
import json
city = input("Enter your city : ")
url = 'https://goweather.herokuapp.com/weather/'
url = url+city
response = rq.get(url)
response = response.text
data = json.loads(response)
print("Temperature in the given city is =>",data.get('temperature'))
print("Wind Speed in the given city is  =>",data.get('wind'))
print("Weather in the given city is     =>",data.get('description'))
