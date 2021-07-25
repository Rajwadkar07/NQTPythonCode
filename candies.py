candies = 10
buy = int(input("Enter the number of candies to buy: "))
if buy in range(1,6):
	print("Number of candies bought:", buy)
	print("Number of candies remaining in the jar:", candies-buy)
else:
	print("Invalid Input")
	print("Number of candies remaining in the jar:", candies)