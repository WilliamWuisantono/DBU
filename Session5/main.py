import requests
import csv
import operator

# API URL for weather data (Berlin, for example)
api_url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

# Send request to the Open-Meteo API
response = requests.get(api_url)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant data from JSON response
    hourly_data = data['hourly']
    temperatures = hourly_data['temperature_2m']
    humidity = hourly_data['relative_humidity_2m']
    wind_speed = hourly_data['wind_speed_10m']
    time = hourly_data['time']

    # Prepare data for CSV (combine the relevant fields)
    weather_data = []
    for i in range(len(time)):
        weather_data.append({
            'time': time[i],
            'temperature_2m': temperatures[i],
            'relative_humidity_2m': humidity[i],
            'wind_speed_10m': wind_speed[i]
        })

    # Sort data by temperature_2m using operator.itemgetter
    sorted_data = sorted(weather_data, key=operator.itemgetter('temperature_2m'))

    # Write sorted data to CSV
    with open('weather_data_operator_sorted.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['time', 'temperature_2m', 'relative_humidity_2m', 'wind_speed_10m'])
        writer.writeheader()
        writer.writerows(sorted_data)

    print("Data successfully written to weather_data_operator_sorted.csv using operator.itemgetter.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
