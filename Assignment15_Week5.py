# Import relevant libraries. ET to arrange xml data and urllib to prevent bad data extraction accessing web data

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

# Ask for user input and protect against bad user input
try:
    xml_data = input("Please enter a URL: ")
except:
    print("Sorry, that didn't work, Luke. ")

# Read in the xml data into a variable "data" using urllib
data = urllib.request.urlopen(xml_data).read()
#convert data into an element tree using fromstring
tree = ET.fromstring(data)
# Find all the comments/comment/counts tags and store in new "lst" variable
lst = tree.findall('comments/comment/count')
# Loop through list and add up the numbers
total = 0
for count in lst:
    total += int(count.text)
# Print the sum
print("Total: ", total)
