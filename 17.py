with open("hightemp.txt", "r") as f:
	unique = set([line.split("\t")[0] for line in f.readlines()])

for u in unique:
	print(u)