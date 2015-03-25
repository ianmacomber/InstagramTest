import operator

d = open("text.txt", "r")
lines = d.readlines()
print(lines)

a = len(lines[0])-1
b = lines[0][1:a]

mydict = {}

#print(mydict, "\n")
#print(type(mydict), "\n")

#print(b)
#print(type(b))

bstrip = b.split(",")

for i in bstrip:
    c, d = i.replace(" ", "").replace('"', '').split(":")
    mydict[c] = int(d)

print(sorted(mydict.items(), key=operator.itemgetter(1)))

try:
    print(mydict['"pandahausofrock"'])
except:
    print("not valid")

try:
    print(mydict['pandahausofrock'])
except:
    print("not valid")
