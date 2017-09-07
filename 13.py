with open("col1.txt", "r") as f:
	col1 = f.readlines()
with open("col2.txt", "r") as f:
	col2 = f.readlines()

col1_2 = [a.replace("\n", "\t")+b for (a, b) in zip(col1, col2)]
with open("col1_2.txt", "w") as f:
	f.writelines(col1_2)