originalNum = input("Enter the number : ")
num = int(originalNum)

#save the number in another variable
temp=num
sumValue=0
f=[0]*10
f[0]=1
f[1]=1
for i in range(2,10): #precomputing the factorial value from 0 to 9 and store in the array.
    f[i]=f[i-1]*i

#Implementation
while(temp):
    r=temp%10 #r will have the value of the unit digit
    temp=temp//10
    sumValue+=f[r] #adding all the factorial
    
print(f"{num} is a strong number" if sumValue == num else f"{num} is not a strong number")

# Method - 2

sumValue=0 
num = int(originalNum)
def Factorial(num):
    if num<=1: 
        return 1 
    else: 
        return num*Factorial(num-1) 
    

def check_StrongNumber(num, sumValue): 
    if num <= 0:
        return sumValue
    
    fact = 1
    rem = num % 10
    fact = Factorial(rem)
    sumValue+=fact
    return check_StrongNumber(num // 10, sumValue)

print(f"{num} is a strong number" if check_StrongNumber(num, sumValue) == num else f"{num} is not a strong number")

