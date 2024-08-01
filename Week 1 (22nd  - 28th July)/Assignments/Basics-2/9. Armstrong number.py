originalNum = input("Enter the number : ")
num = int(originalNum)

digit, sumValue = 0, 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)
  num = num/10
  sumValue += pow(digit,length)

num = int(originalNum)
  
print(f"{num} is a Armstrong" if num == sumValue else f"{num} is not Armstrong")

# Method - 2
num = int(originalNum)
sumValue = 0
length = len(str(num))

def checkArmstrong(num,length,sum):
  if num == 0:
    return sum
  sum += pow(int(num % 10), length)
  return checkArmstrong(num/10, length, sum)

num = int(originalNum)

print(f"{num} is a Armstrong" if num == checkArmstrong(num, length, sumValue) else f"{num} is not Armstrong")