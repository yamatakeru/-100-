with open("hightemp.txt", "r") as f:
	text = f.read().replace('\t', ' ')

print(text)