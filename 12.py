with open("hightemp.txt", "r") as f:
	lines = f.readlines()

col1 = []
col2 = []
for line in lines:
	temp = line.split("\t")
	col1.append(temp[0]+"\n")
	col2.append(temp[1]+"\n")

with open("col1.txt", "w") as f:
	f.writelines(col1)
with open("col2.txt", "w") as f:
	f.writelines(col2)
