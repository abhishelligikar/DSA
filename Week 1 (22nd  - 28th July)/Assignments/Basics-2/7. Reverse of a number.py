originalNum = input("Enter the number : ")
num = int(originalNum)

temp = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num //= 10
    
print(reverse)

# Method - 2
num = int(originalNum)
print(str(num)[::-1])

# Method - 3
num = int(originalNum)
reverse = 0

def reverse_number(num, reverse):
    if num == 0:
        return reverse
    
    remainder = int(num % 10)
    reverse = (reverse * 10) + remainder
    return reverse_number(int(num/10), reverse)

print(reverse_number(num, reverse))