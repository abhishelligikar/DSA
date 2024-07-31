num = int(input("Enter the number : "))
isPrime = True

# Method 1 : Iterative
if num < 2:
    isPrime = False
else:
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    
print(f"{num} is a prime number" if isPrime else f"{num} is not a prime number")

# Method 2 : Optimization by n/2 ietrations
isPrime = True
if num < 2:
    isPrime = False
else:
    for i in range(2, int((num/2)+1)):
        if num % i == 0:
            isPrime = False
            break
    
print(f"{num} is a prime number" if isPrime else f"{num} is not a prime number")

# Method 3 : Optimization by SquareRoot of n
isPrime = True
if num < 2:
    isPrime = False
else:
    for i in range(2, int(pow(num,0.5)+1)):
        if num % i == 0:
            isPrime = False
            break
    
print(f"{num} is a prime number" if isPrime else f"{num} is not a prime number")

# Method 4 : Skipping Even Iteration
isPrime = True
if num < 2:
    isPrime = False
else:
    for i in range(2, int((num/2)+1),2):
        if num % i == 0:
            isPrime = False
            break
    
print(f"{num} is a prime number" if isPrime else f"{num} is not a prime number")

# Method 5 : Recursion
def check_prime_number(num, iter=2):
    if num == iter:
        return True
    if num % iter == 0:
        return False
    if num < 2:
        return False
    else:
        return check_prime_number(num, iter+1)
    
print(f"{num} is a prime number" if check_prime_number(num) else f"{num} is not a prime number")