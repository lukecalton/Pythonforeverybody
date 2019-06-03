#sets count and total to 0
count = 0
total = 0

#use of try and except prevents crashing from bad user input
try:
    fname = input("Please enter a file name:   ")

except:
    print("Please enter a valid file name")

#opens file
fh = open(fname)

#Creates empty list
mylist = list()

#for loop reads file line by line looking for the relevant data
for line in fh:
    emails = line.rstrip().split(" ")
    #if formula to find each relevant line
    if element in line.startswith("From "): continue
    element.append(mylist)
    #increment the counter
    count = count + 1
    #find hint
    x = line.find("From ")
    #take emails +1 right from the "from"
    y = line[1:]
    #strip empty space
    mylist.append(y)

print(mylist)
print("There were",count,"lines in the file with From as the first word")
