final = []
a = 0
b = 0

for i in range(1,10):
    final.append(a)
    final.append(b)
    a = a + 2
    b = b + 1

opt = int(input("Enter choice: "))
print(final[opt-1])
