n = int(input("Enter number of elements: "))
elem = []
for i in range(n):
    elem.append(int(input()))
k = int(input("Enter element to find: "))
print("Present at index", elem.index(k))
