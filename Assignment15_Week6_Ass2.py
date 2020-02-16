# Import relevant libraries. JSON and urllib to prevent bad data extraction accessing web data
import json
import urllib.request, urllib.parse, urllib.error

# API key is required to access the API, or the data from the API stored elsewhere
api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else :
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'


# Prompt for the location
while True:
    address = input("Please enter a location, Luke: ")
    if len(address) < 1 : break

    url = service_url + urllib.parse.urlencode(
    {'address': address})

# If an API key is required
    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = service_url + urllib.parse.urlencode(parms)


# Encode, decode data taken from the web in UTF8

    encoded_data = urllib.request.urlopen(url)
# Convert into unicode
    decoded_data = encoded_data.read().decode()

# Load the JSON data into a variable JS
    try:
        js = json.loads(decoded_data)
    except:
        js = None

# Protect against anything strange

    if not js or "status" not in js or js["status"] != "OK":
        print("Sorry Luke, this didn't work. Check your code.")
        print(decoded_data)
        continue

# Print the JSON data with an indent
    print(json.dumps(js, indent=4))

# Extract relevant data from JSON
    place_id = js["results"][0]["place_id"]

# Print relevant data
    print("Place I.D :", place_id)
