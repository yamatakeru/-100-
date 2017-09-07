import sys

N = int(sys.argv[1])
with open("hightemp.txt", "r") as f:
	lines = f.readlines()

l = len(lines) // N
for i in range(N):
	with open("s{}.txt".format(i), "w") as f:
		f.writelines("".join(lines[l*i:l*(i+1)]))