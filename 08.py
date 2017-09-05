def cipher(data):
	return "".join([chr(219-ord(c)) if c.islower() else c for c in data])

data = "ABCdef123"
print(data)
result = cipher(data)
print(result)
print(cipher(result))