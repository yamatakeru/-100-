string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
temp = string.split(" ")
result = {s[:1] if i+1 in [1,5,6,7,8,9,15,16,19] else s[:2]: i+1 for (i, s) in enumerate(temp)}

print(result)