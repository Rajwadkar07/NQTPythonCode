limit = int(input("Enter Number: "))
series = []
series.append(1)
series.append(1)
print(len(series))
if len(series)>limit:
    pass
else:
    for i in range(limit-2):
        num1 = series[len(series)-1]
        num2 = series[len(series)-2]
        sum = num1+num2
        series.append(sum)
print(series)
