import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Request user input for URL and then "soup" it to make it work
url = input("Please enter a URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# get user input for how many times to search between websites
count = int(input('How many times should I follow the links?: '))

# What position of the URL list would you like me to extract?
position = int(input('What position of the URL list would you like me to extract? :'))-1

# loop to go through the HTMLs
while count >= 0:
    # re-reads the current url
    html = urllib.request.urlopen(url, context=ctx).read()
    # creates a new soup object
    soup = BeautifulSoup(html, 'html.parser')
    # searches the page for all <a> tags
    tags = soup('a')
    print("Retrieving: ", url)
    # upates the current url
    url = tags[position].get("href", None)
    count = count - 1
