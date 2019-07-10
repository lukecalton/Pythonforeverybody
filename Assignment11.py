#import relevant Regular Expression Library
import re

#try and except to read in file and protect against bad user input
try:
    fname = input("Please enter a file name:   ")

except:
    print("Please enter a valid file name")

#opens file
fh = open(fname)

#empty total

total = 0

#for loop to look through each line of the file

for line in fh:
    #with re to extact strings and starts with any number of characters
    numbers = re.findall("[0-9]+", line)
    #converts and creates list of integers
    integers = list(map(int, numbers))
    #loop through list of integers and add them up
    for x in integers:
        total = total + x

print(total)
