# Import relevant libraries. JSON and urllib to prevent bad data extraction accessing web data
import json
import urllib.request, urllib.parse, urllib.error

# Ask for user input and protect against bad user input
try:
    json_data = input("Please enter a URL: ")
except:
    print("Sorry, that didn't work, Luke. ")

#initialise a total of 0
total = 0

json_data = urllib.request.urlopen(json_data).read()
#parse JSON into a dictionary
parsed_json = json.loads(json_data)
#create dictionary of relevant numbers
parsed_json = parsed_json["comments"]
#for loop to iterate through each line, extract the counts and add to total
for item in parsed_json:
    total =+ total + int(item["count"])
print(total)
