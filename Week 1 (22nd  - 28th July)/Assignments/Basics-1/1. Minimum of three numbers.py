

# Method 1 : Defining Values
a, b, c = 1, 4, 2

if(a <= b and a <= c):
    print(a, 'is the smalent number')
elif(b <= a and b <= c):
    print(b, 'is the smallest number')
else:
    print(c, 'is the smallest number')
    
# Method 2 : Defining Values with function
def findSmallestNumber(a,b,c):
    if(a <= b and a <= c):
        print(a, 'is the smalent number')
    elif(b <= a and b <= c):
        print(b, 'is the smallest number')
    else:
        print(c, 'is the smallest number')
        
findSmallestNumber(4, 2, 0)

# Method 3 : Taking input from user with function
a, b, c = map(int, input("Enter three interger values seaparated by space: ").split())
print("a value is ", a)
print("b value is ", b)
print("c value is ", c)
findSmallestNumber(a, b, c)
