originalNum = input("Enter the number : ")
num = int(originalNum)

def checkHarshad(n):
    sumValue = 0
    temp = n
    while temp > 0:
        sumValue = sumValue + temp % 10
        temp = temp // 10

    # Return true if sum of digits is multiple of n
    return n % sumValue == 0

print(f"{num} is a Harshad number" if checkHarshad(num) else f"{num} is not a Harshad number")

# Method - 2
sumValue = 0
num = int(originalNum)

def checkHarshad(n):
    # Converting integer to string
    st = str(n)
    sumValue = 0

    for i in st:
        sumValue = sumValue + int(i)
        
    return n % sumValue == 0

print(f"{num} is a Harshad number" if checkHarshad(num) else f"{num} is not a Harshad number")