originalNum = input("Enter the number : ")
num = int(originalNum)

n1, n2, last_term_number = 0, 1, 0
for i in range(num):
    last_term_number = n1 + n2
    n1 = n2
    n2 = last_term_number
   
print(f"{num}th term of the fibonacci series is {last_term_number}") 
    
# Method - 2
def getFibonacciNumberToNTerms(num):
    if num <= 2:
        return num
    else:
        return getFibonacciNumberToNTerms(num -1) + getFibonacciNumberToNTerms(num - 2)
   

print(f"{num}th term of the fibonacci series is {getFibonacciNumberToNTerms(num)}")
    
    