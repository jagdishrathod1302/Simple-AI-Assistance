
from datetime import datetime
import requests

print("TOOLS MODULE IS LOADING")

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_city_weather(city):
    url = f"http://wttr.in/{city}?format=3"
    response = requests.get(url,timeout=10)
    return response.text

def get_user_city():
    return "Banglore"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Returns the current date and time.",
            "parameters": {
                "type": "object",
                "properties": {},
                
            },
        },
    },
    {
        "type":"function",
        "function":{
            "name":"get_city_weather",
            "description":"Returns the current weather for a city",
            "parameters":{
                "type":"string",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"City to get the wheather for"
                    }
                },
            },
        },
    },
    {
        "type":"function",
        "function":{
            "name":"get_user_city",
            "description":"Returns the city where the user is live. Use the this when user says my city  where I live what is my city, my location without naming the city.",
            "parameters":{"type":"string","properties":{}},
        },
    },
]

FUNCTION_NAME_TO_FUNCTION_MAP = {
    "get_current_time": get_current_time,
    "get_city_weather":get_city_weather,
    "get_user_city":get_user_city,
}

print("TOOLS DEFINED SUCCESSFULLY")
