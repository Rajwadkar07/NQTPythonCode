import math
orders = int(input("Orders: "))
x = math.ceil(orders/2)
y = x
a = [1, 4, 3, 2, 7, 5, 9, 6]
b = [1, 2, 3, 6, 5, 4, 9, 8]
waiter_l = []
tip = 0
for i in range(len(a)):
    if a[i]>b[i] or a[i]==b[i]:
        waiter = "Rahul"
        waiter_l.append(1)
    else:
        waiter = "Ankit"
        waiter_l.append(2)
for i in range(orders):
    if waiter_l[i] == 1:
        tip += a[i]
    elif waiter_l[i] == 2:
        tip += b[i]
print(tip)
