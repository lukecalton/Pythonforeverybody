#sets count and total to 0
count = 0
total = 0

#use of try and except prevents crashing from bad user input

try:
    fname = input("Please enter the file name:   ")
except:
    print("Please enter a valid file name")
#opens file
fh = open(fname)
# for loop reads file line by line looking for the relevant data
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
#increment the counter
    count = count + 1
#find the colon
    x = line.find(":")
#take strings +1 right from the colon
    y = line[x+1: ]
#strip empty space
    y = y.lstrip()
#convert integer to float
    z = float(y)
#math starts
    total = total + z
#print calculation
print ("Average spam confidence:", total / count)
