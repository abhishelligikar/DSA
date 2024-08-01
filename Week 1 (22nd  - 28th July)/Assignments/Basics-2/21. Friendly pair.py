num1, num2 = map(int, input("Enter the range of number separted by '-' : ").split("-"))


def printDivisors(n, factors) :
    i = 1
    while i <= n :
        if (n % i==0) :
            factors.append(i)
        i = i + 1
    return sum(factors) - n

if int(printDivisors(num1, [])/num1) == int(printDivisors(num2, [])/num2):
    print(f"{num1} and {num2} are Friendly pair")
else:
    print(f"{num1} and {num2} are not a Friendly Pair")
    

# Method - 2

def printDivisors(n, factors) :
     
    # Note that this loop runs till square root
    i = 1
    while i <= pow(n,0.5):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                factors.append(i)
            else :
                # Otherwise print both
                factors.append(i)
                factors.append(int(n/i))
        i = i + 1
    return sum(factors) - n

if int(printDivisors(num1, [])/num1) == int(printDivisors(num2, [])/num2):
    print(f"{num1} and {num2} are Friendly pair")
else:
    print(f"{num1} and {num2} are not a Friendly Pair")