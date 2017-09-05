def n_gram(data, n):
	return [data[i:i+n:] for i in range(len(data)-n+1)]

string1 = "paraparaparadise"
string2 = "paragraph"
X = set(n_gram(string1, 2))
Y = set(n_gram(string2, 2))
print(X, Y)
print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)