originalNum = input("Enter the number : ")
num = int(originalNum)

temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

print(f"{num} is a Palindrome" if num == reverse else f"{num} is not Palindrome")
  
# Method - 2
reverse = int(str(num)[::-1])

print(f"{num} is a Palindrome" if num == reverse else f"{num} is not Palindrome")

# Method - 3
num = int(originalNum)
reverse = 0

def recurrev(number, rev):
    if number == 0:
        return rev

    remainder = int(number % 10)
    rev = (rev * 10) + remainder

    return recurrev(int(number / 10), rev)

reverse = recurrev(num, reverse)

print(f"{num} is a Palindrome" if num == reverse else f"{num} is not Palindrome")

# Method - 4
num = originalNum

def checkPalindrome(str):

    # check if str[i] is same as str[len(str) - i - 1]
    # for whole string
    for i in range(0, len(str)):

        # Basically, we are checking i-th character is
        # same as i-th character from the end or not
        if str[i] != str[len(str) - i - 1]:
            return False

    return True

print(f"{num} is a Palindrome" if checkPalindrome(num) else f"{num} is not Palindrome")


# Method - 5
num = originalNum

# we do not need to check the whole string
# only till the mid of string
# as if it palindrome the first half == second half of string when read backwards
def checkPalindrome(str):

    # Run loop from 0 to len/2
    mid = int(len(str) / 2)

    for i in range(0, mid):
        if str[i] != str[len(str) - i - 1]:
            return False

    return True

print(f"{num} is a Palindrome" if checkPalindrome(num) else f"{num} is not Palindrome")


# Method - 6
num = originalNum

def checkPalindrome(str):
    # using inbuilt reversed function
    reverse = ''.join(reversed(str))

    if str == reverse:
        return True

    return False

print(f"{num} is a Palindrome" if checkPalindrome(num) else f"{num} is not Palindrome")

# Method - 7
num_string = originalNum
rev = ""
for char in num_string:
    rev = char + rev

print(f"{num} is a Palindrome" if num_string == rev else f"{num} is not Palindrome")


# Method - 8
num_string = originalNum
j = -1
flag = 0
for char in num_string:
    # char starts from index 0
    # string[j] forces to read from end
    # bcz negative index are read from end
    if char != num_string[j]:
        flag = 1
        break
    j = j - 1
    
print(f"{num} is not Palindrome" if flag else f"{num} is a Palindrome")


# Method - 9
num_string = originalNum
n = len(num_string)
c = []
for i in range(n - 1, -1, -1):
    c.append(num_string[i])

rev = "".join(c)

print(f"{num} is a Palindrome" if num_string == rev else f"{num} is not Palindrome")
