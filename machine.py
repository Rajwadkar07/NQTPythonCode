weight = int(input("Enter weight: "))
if weight<=2000:
	print("25 minutes")
elif weight<4000 and weight>2001:
	print("35 minutes")
elif weight>4000 and weight<7000:
	print("45 minutes")
elif weight>=7000:
	print("Overload")
else:
	print("Invalid input")