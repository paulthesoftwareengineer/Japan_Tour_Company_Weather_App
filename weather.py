import requests

# Set the API endpoint and your API key
endpoint = 'https://api.weather.com/v1/geocode/{latitude}/{longitude}/forecast/hourly/48hour.json'
api_key = 'YOUR_API_KEY'

# Set the latitude and longitude of the location you want to get the forecast for
latitude = '37.33'
longitude = '-121.89'

# Construct the URL with the endpoint, API key, and location
url = endpoint.format(latitude=latitude, longitude=longitude) + '?apiKey=' + api_key

# Send a GET request to the API and store the response
response = requests.get(url)

# Print the forecast data
forecast_data = response.json()
print(forecast_data)
