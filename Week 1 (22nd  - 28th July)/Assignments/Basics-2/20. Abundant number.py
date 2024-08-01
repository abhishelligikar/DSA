originalNum = input("Enter the number : ")
num = int(originalNum)

sumValue = 1 # 1 can divide any number 

for i in range(2, num):
  if(num % i == 0):    #if number is divisible by i add the number 
   sumValue = sumValue + i

print(f"{num} is a Abundant number" if sumValue > num else f"{num} is not a Abundant number")