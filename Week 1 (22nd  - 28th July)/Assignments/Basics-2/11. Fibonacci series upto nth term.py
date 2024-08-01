originalNum = input("Enter the number : ")
num = int(originalNum)

n1, n2 = 0, 1
for i in range(num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end = ' ')
   
print() 
    
# Method - 2
def getFibonacciNumberToNTerms(num):
    if num <= 2:
        return num
    else:
        return getFibonacciNumberToNTerms(num -1) + getFibonacciNumberToNTerms(num - 2)
   
for i in range(1, num +1):
    print(getFibonacciNumberToNTerms(i), end = ' ')
    
    