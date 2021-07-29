a = input()
b = input()
c = input()
vowels = "aeiou"
for i in a:
    if i in vowels:
        a = a.replace(i, "%")
for i in b:
    if i not in vowels:
        b = b.replace(i, "#")
print(b)
c = c.upper()
print(a+b+c)
