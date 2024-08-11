import requests

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

data = response.json()

print("Latitude:", data['iss_position']['latitude'])
print("Longitude:", data['iss_position']['longitude'])
print("Timestamp:", data['timestamp'])