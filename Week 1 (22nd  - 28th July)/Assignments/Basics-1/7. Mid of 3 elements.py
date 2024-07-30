a,b,c = map(int, input("Enter 3 numbers : ").split(","))
print(f"Value of a : {a} \n" f"Value of b : {b} \n" f"Value of c : {c}")

def middle_of_three_numbers(a,b,c):
    if ((a <= b <= c) or (c <= b <= a)):
        return b
    elif ((b <= a <= c) or (c <= a <= b)):
        return a
    else:
        return c
    
print(f"Middle of {a}, {b} and {c} is : {middle_of_three_numbers(a,b,c)}")

def mid(a,b,c):
    num = [a,b,c]
    small,big = min(num), max(num)
    num.remove(small)
    num.remove(big)
    return num[0]

print(f"Middle of {a}, {b} and {c} is : {mid(a,b,c)}")

def middle(a,b,c):
    numbers = [a,b,c]
    return sorted(numbers)[len(numbers)//2]

print(f"Middle of {a}, {b} and {c} is : {middle(a,b,c)}")