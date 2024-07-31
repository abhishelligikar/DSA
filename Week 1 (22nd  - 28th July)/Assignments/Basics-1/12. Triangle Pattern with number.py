# Write a program to display a pattern like a triangle using an number.

# The Pattern Like:

#    1
#   1 2
#  1 2 3
# 1 2 3 4

n = int(input("Enter number of lines triangle to have : "))
previous = ''
for i in range(1, n+1):
    s = ' ' * (n-i)
    print(s, end = '')
    previous += f"{i} "
    print(previous) 
    
    
for i in range(1, n+1):
    s = ' ' * (n-i)
    print(s, end = '')
    print(f"{i} " * i)  
