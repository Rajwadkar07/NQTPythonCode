num = str(input("Number: "))
nums = []
odd = 0
even = 0
for i in num:
    nums.append(i)
for i in range(0,len(nums),2):
    odd += int(nums[i])
for i in range(1,len(nums),2):
    even += int(nums[i])
diff = even - odd
print(abs(diff))
