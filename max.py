a = input("Enter: ")
print(a.split())
max = 0
for i in a.split():
    try:
        if int(i)>max and "9" not in str(i):
            max = int(i)
    except ValueError:
        pass
print(max)
