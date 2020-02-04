f = open("in.txt", "r")
line = f.readline()
while line != "":
	print line
	line = f.readline()
f.close()
