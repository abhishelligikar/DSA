low, high = map(int, input("Enter the range of number separted by '-' : ").split("-"))
primes = []


for i in range(low, high, 1):
    isPrime = True
    
    if i < 2:
        continue
    if i == 2:
        primes.append(i)
        continue
    
    for x in range(2, i):
        if i % x == 0:
            isPrime = False
            break
    
    if isPrime:
        primes.append(i)
        
print(primes)


# Method - 2
primes = []
for i in range(low, high + 1):
    isPrime = True
    
    if i < 2:
        isPrime = False
    
    if i % 2 == 0:
        continue
    iter = 2
    
    while iter < int(i / 2):
        if i % iter == 0:
            isPrime = False
            break
        iter += 1
        
    if isPrime:
        primes.append(i)
        
print(primes)


# Method - 3
primes = []
for i in range(low, high + 1):
    isPrime = True
    
    if i < 2:
        isPrime = False
    
    if i % 2 == 0:
        continue
    
    if i % 3 == 0:
        continue
    
    iter = 2
    while iter < int(pow(i, 0.5)+1):
        if i % iter == 0:
            isPrime = False
            break
        iter += 1
        
    if isPrime:
        primes.append(i)
        
print(primes)


# Method - 3
primes = []
for i in range(low, high + 1):
    isPrime = True
    
    if i < 2:
        isPrime = False
    
    if i % 2 == 0:
        continue
    
    if i % 3 == 0:
        continue
    
    iter = 3
    while iter < int(pow(i, 0.5)+1):
        if i % iter == 0:
            isPrime = False
            break
        iter += 2
        
    if isPrime:
        primes.append(i)
        
print(primes)
        
    