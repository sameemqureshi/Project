import requests

# Define the URL of your API endpoint
url = 'http://127.0.0.1:8080/entitydata'

# Define the data to be sent in the request
data = {
    'entity_id': 133,
    'physical_quantity': 'temperature',
    'metric': 'k',
    'value': 100,
    'ts': 2024-11-7
}

# Send a POST request to the API endpoint
response = requests.post(url, data)


# Print the response
print(response.status_code)  # Print the status code of the response
   # Print the JSON response from the server
