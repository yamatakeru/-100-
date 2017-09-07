with open("hightemp.txt", "r") as f:
	lines = [(line, line.split("\t")[2]) for line in f.readlines()]

result = "".join([line for (line, t) in sorted(lines, key=lambda l: l[1], reverse=True)])
print(result)