with open("hightemp.txt", "r") as f:
	col1 = [line.split("\t")[0] for line in f.readlines()]

prefecture = {p: 0 for p in set(col1)}
for p in col1:
	prefecture[p] += 1

result = "\n".join([p for (p, c) in sorted(prefecture.items(), key=lambda p: p[1], reverse=True)])
print(result)