start, end = map(int,input("Enter start and end numbers of range : ").split(","))
sum = 0

# Using loop
for i in range(start, end + 1):
    sum += i

print(f"Sum of numbers in a given range is : {sum}")

# Using formula

print(f"Sum of numbers in a given range is : {(end*(end+1)/2) - (start*(start+1)/2) + start}")

# Using recursion
sum = 0
def getSum(sum, start, end):
    if start > end:
        return sum
    return start + getSum(sum, start + 1, end)

print(f"Sum of numbers in a given range is : {getSum(sum, start, end)}")