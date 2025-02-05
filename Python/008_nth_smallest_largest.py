l1=[76, 23, 45, 12, 54, 9] 
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
	for j in range(i+1, len(l1)):
		if l1[i] >= l1[j]:
			l1[i], l1[j] = l1[j],l1[i]

# sorted list
print("Sorted List", l1)

# nth smallest number
n = int(input("Enter the nth smallest number: "))
print(f"The {n}th smallest number is: {l1[n-1]}")

# nth largest number
n = int(input("Enter the nth largest number: "))
print(f"The {n}th largest number is: {l1[-n]}")


print("========================================")
# Another way to find nth smallest and largest number

def nth_largest(nums, n): # function to find nth largest number
    for i in range(n):  # loop to find nth largest number
        max_num = nums[0]
        for num in nums: 
            if num > max_num:
                max_num = num
        nums.remove(max_num)
    return max_num

def nth_smallest(nums, n): # function to find nth smallest number
    for i in range(n): # loop to find nth smallest number
        min_num = nums[0]
        for num in nums:
            if num < min_num:
                min_num = num
        nums.remove(min_num)
    return min_num

nums = [7, 2, 5, 1, 9, 3, 8]
n = int(input("Enter the value of n: "))
print(f"The {n}rd largest number is:", nth_largest(nums.copy(), n))
print(f"The {n}rd smallest number is:", nth_smallest(nums.copy(), n))

print("========================================")
