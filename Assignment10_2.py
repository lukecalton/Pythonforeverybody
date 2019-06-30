#use of try and except prevents crashing from bad user input
try:
    fname = input("Please enter a file name:   ")

except:
    print("Please enter a valid file name")

#opens file
fh = open(fname)

counts = dict()
#for loop reads file line by line looking for the relevant data

for line in fh:
    eachline = line.rstrip()
    words = line.split()
    #protect against empty array
    if len(words) < 1:
        continue
    if words[0] != 'From' :
        continue
    time = (words[5])
    hour = time.split(":")
    hr = (hour[0])
    counts[hr] = counts.get(hr,0) + 1

x = sorted(counts.items())

for key,value in x :
    print(key,value)






#maximum = 0
#max_key = None

#for k in counts:
#    if counts[k] > maximum:
#        maximum = counts[k]
#        max_key = k

#print(max_key, maximum)
