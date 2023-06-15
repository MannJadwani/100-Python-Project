import pip._vendor.requests as requests
import json
import os 


city= input("enter the name of the city: ")

url=f"http://api.weatherapi.com/v1/current.json?key=98280977eca249b0b0c113700231506&q={city}"

r=requests.get(url)

# print(r.text)
wdic= json.loads(r.text)

currentTemp = wdic["current"]["temp_c"]
print(currentTemp)
os.system(f"say 'the Current temprature in {city} is {currentTemp} '")


