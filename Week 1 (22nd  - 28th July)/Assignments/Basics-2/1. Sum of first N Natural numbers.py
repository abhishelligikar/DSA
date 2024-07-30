num = int(input("Enter the number : "))
sum = 0

# Using loop
for i in range(1, num + 1):
    sum += i

print(f"Sum of first N natural numbers is : {sum}")

# Using formula

print(f"Sum of first N natural numbers is : {(num*(num+1))/2}")

# Using recursion

def getSum(num):
    if num == 1:
        return 1
    return num + getSum(num-1)

print(f"Sum of first N natural numbers is : {getSum(num)}")