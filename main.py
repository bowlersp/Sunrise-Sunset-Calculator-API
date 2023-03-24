# #How to use an API get to find the current ISS location
import requests
from datetime import datetime
my_lat = "38.627003"
my_long = "-90.199402"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# print(data)

# #How to filter the data to get just the latitude and longitude

# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]

# iss_position = (latitude, longitude)
# print(iss_position)


#Sunset and Sunrise Times API below

parameters = {
  "lat": my_lat,
  "lng": my_long,
  "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"Sunrise is at {sunrise}")
print(f"Sunset is at {sunset}")

time_now = datetime.now()
print(f"Current time is {time_now}")
