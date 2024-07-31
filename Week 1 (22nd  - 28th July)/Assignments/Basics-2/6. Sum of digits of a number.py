originalNum = input("Enter the number : ")
num = originalNum
sumValue = 0

for i in num:
    sumValue += int(i)
    
print(sumValue)

# Method - 2 
num = int(originalNum)
sumValue = 0

while num != 0:
    digit = int(num%10)
    sumValue += digit
    num /= 10
    
print(sumValue)

# Method - 3
num = int(originalNum)
sumValue = 0
def findsumValue(num, sumValue):
    if num == 0:
        return sumValue
    
    digit = int(num%10)
    sumValue += digit
    return findsumValue(num/10, sumValue)

print(findsumValue(num, sumValue))

# Method - 4
num = int(originalNum)
sumValue = 0
def findsumValue(num):
    if num == 0:
        return 0
    
    return int(num % 10) + findsumValue(num/10)

print(findsumValue(num))

# Method - 5
num = int(originalNum)
sumValue = 0

for i in range(len(str(num))):
    sumValue += ord(str(num)[i]) - 48    # ord methods helps with ASCII
    
print(sumValue)

# Method - 6
num = int(originalNum)
sumValue = 0

def getsumValue(num):
    num_string = str(num)       # convert into string
    
    # fetch each individual char using strip method
    # find comparable int and store it in map
    # covert it into list
    list_of_number = list(map(int, num_string.strip())) 
    
    return sum(list_of_number)

print(getsumValue(num))

# Method - 7        # One line recursive
num = int(originalNum)
sumValue = 0

def sumDigits(n):
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n / 10)) 
   
print(sumDigits(num))

# Method - 8
num = int(originalNum)
sumValue = 0

list_of_num = [int(d) for d in input("Enter the number : ")]
print(sum(num))
