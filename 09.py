import random as rd

string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(string)
result = " ".join([s[0]+"".join(rd.sample(list(s[1:-1]), len(s[1:-1])))+s[-1] if len(s) > 4 else s for s in string.split(" ")])
print(result)