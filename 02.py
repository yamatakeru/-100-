string1 = "パトカー"
string2 = "タクシー"
result = "".join([a+b for (a, b) in zip(string1, string2)])

print(result)