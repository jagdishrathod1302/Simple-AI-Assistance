
from datetime import datetime
import requests

print("TOOLS MODULE IS LOADING")

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_city_weather(city):
    url = f"http://wttr.in/{city}?format=3"
    response = requests.get(url,timeout=10)
    return response.text

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
    }
]

FUNCTION_NAME_TO_FUNCTION_MAP = {
    "get_current_time": get_current_time,
    "get_city_weather":get_city_weather
}

print("TOOLS DEFINED SUCCESSFULLY")
