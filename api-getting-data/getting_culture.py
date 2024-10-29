import requests
import apikey
import os
import json
import pyeuropeana.apis as apis

# Fetch data from the first API
url = 'https://anapioficeandfire.com/api/houses/362'
response = requests.get(url)
response_data = response.json()
print(response_data)

# Save and load the Europeana API key
apikey.save("EUROPEANA_API_KEY", "INSERT_YOUR_API")
europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

# Fetch data from the Europeana API
response_euro = apis.entity.suggest(
   text='Dubrovnik',
   TYPE='place',
)
print(response_euro)

# Combine the data into a dictionary
data = {
    "response": response_data,
    "response_euro": response_euro
}

# Write the data to a JSON file
with open('getting_culture.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("API data has been written to getting_culture.json.")

