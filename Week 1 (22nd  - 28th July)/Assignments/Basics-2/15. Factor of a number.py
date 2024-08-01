import math


originalNum = input("Enter the number : ")
num = int(originalNum)

def find_factors_of_number(num):
    i = 1
    while i <= num:
        if (num % i == 0):
            print(i, end = ' ')
        i += 1
        
print(find_factors_of_number(num))

# Method - 2
def printDivisors(n) :
     
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                print (i,end=" ")
            else :
                # Otherwise print both
                print (i , int(n/i), end=" ")
        i = i + 1
        
print(printDivisors(num))