originalNum = input("Enter the number : ")
num = int(originalNum)

sumValue = 0
for i in range(1, num):
    if num % i == 0:
        sumValue += i
        
print(f"{num} is a perfect number" if num == sumValue else f"{num} is not a perfect number")

# Method  - 2
sumValue = 0
num = int(originalNum)
for i in range(1, num//2 + 1):
    if num % i == 0:
        sumValue += i
        
print(f"{num} is a perfect number" if num == sumValue else f"{num} is not a perfect number")

# Method - 3
sumValue = 0
num = int(originalNum)
def FindPerfectNumber(num, iter):                       #def FindPerfectNumber(num, iter, sumValue):
    global sumValue                                     #   
    if iter <= num//2:                                  #   if iter <= num//2:
        if num % iter == 0:                             #       if num % iter == 0:
            sumValue += iter                            #           sumValue += iter
                                                        #
        FindPerfectNumber(num, iter + 1)                #      return FindPerfectNumber(num, iter + 1, sumValue)
                                                        #
    return sumValue                                     #   return sumValue

print(f"{num} is a perfect number" if num == FindPerfectNumber(num, 1) else f"{num} is not a perfect number")      