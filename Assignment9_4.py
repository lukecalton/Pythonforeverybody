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
    emails = (words[1])
    counts[emails] = counts.get(emails,0) + 1

maximum = 0
max_key = None

for k in counts:
    if counts[k] > maximum:
        maximum = counts[k]
        max_key = k

print(max_key, maximum)
