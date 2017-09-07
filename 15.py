import sys

N = int(sys.argv[1])
with open("hightemp.txt", "r") as f:
	result = "".join(f.readlines()[-N:])

print(result)