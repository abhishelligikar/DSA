start, end = map(int,input("Enter start and end numbers of N Natural numbers : ").split(","))
sum = 0

# Using loop
for i in range(start, end + 1):
    sum += i

print(f"Sum of first N natural numbers is : {sum}")

# Using recursion

def getSum(end):
    if end == start:
        return start
    return end + getSum(end-1)

print(f"Sum of first N natural numbers is : {getSum(end)}")