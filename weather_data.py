import requests,json

base_URL = "https://api.openweathermap.org/data/2.5/weather?"

print("Enter API:")
API= input()

options = ["By City Name", "By Geographic coordinates"]
print("Choose to Search By City name or geographic coordinates: ")

for i in range(2):
    print(str(i) + ":" + options[i])
choice = input()

if(choice == "0"):

    print("Enter city name:")
    CITY = input()
    URL = base_URL + "q=" + CITY + "&units=metric" + "&appid=" + API
elif(choice == "1"):
    print("Enter Latitude:")
    Lat = input()
    print("Enter Logngitude:")
    Lon = input()
    URL = base_URL + "lat=" + Lat + "&lon=" + Lon + "&units=metric" + "&appid=" + API

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    main = data['main']

    # getting temperature
    temperature = main['temp']
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
    # weather report
    report = data['weather']
    name= data['name']
    print(f"City:{name}")
    print(f"Temperature: {temperature} C")
    print(f"Humidity: {humidity} %")
    print(f"Pressure: {pressure} hPa")
    print(f"Weather Report: {report[0]['description']}")
else:
    # showing the error message
    print("Error in the HTTP request")




