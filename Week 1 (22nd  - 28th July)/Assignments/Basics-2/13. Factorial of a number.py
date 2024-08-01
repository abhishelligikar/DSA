originalNum = input("Enter the number : ")
num = int(originalNum)

factorialValue = 1
for i in range(num, 0, -1):
    factorialValue *= i
    
print(factorialValue)

# Method - 2
def factorial_number(num):
    if num <= 1:
        return 1
    
    return num * factorial_number(num -1)

print(factorial_number(num))