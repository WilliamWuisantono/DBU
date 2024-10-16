import requests
import csv
import operator

api_url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    hourly_data = data['hourly']
    temperature = hourly_data['temperature_2m']
    humidity = hourly_data['relative_humidity_2m']
    wind_speed = hourly_data['wind_speed_10m']
    time = hourly_data['time']

    weather_data = []
    for i in range(len(time)):
        weather_data.append({
            'time': time[i],
            'temperature_2m': temperature[i],
            'relative_humidity_2m': humidity[i],
            'wind_speed_10m': wind_speed[i]
        })

    sorted_data = sorted(weather_data, key=operator.itemgetter('temperature_2m'))


    with open('weather_sorted_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['time', 'temperature_2m', 'relative_humidity_2m', 'wind_speed_10m'])
        writer.writeheader()
        writer.writerows(sorted_data)
    print("Data has been sorted and written in CSV file!")

else:
    print("Failed to retrieve data. Try again.")


#Sources used:
#https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/#
#https://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return-on-windows

