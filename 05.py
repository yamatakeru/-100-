def n_gram(data, n):
	return [data[i:i+n:] for i in range(len(data)-n+1)]

data = "I am an NLPer"
print(n_gram(data, 2))
data = data.split(" ")
print(n_gram(data, 2))