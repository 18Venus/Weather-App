import requests
import json
import pyttsx3

city = input("Enter the name of the city: ")


url = f"https://api.weatherapi.com/v1/current.json?key=5e5030ca07434fee9b4101925242706&q={city}"

r = requests.get(url)

wdic=json.loads(r.text)
x=wdic["current"]["temp_c"]
y=f"The current temperature in {city} is {x} degrees"
engine = pyttsx3.init()
engine.say(y)
engine.runAndWait()


    