# Write a program to display a pattern like a triangle using an number.

# The Pattern Like:

# 1   1
#  2 2
#   3
#  4 4
# 5   5

n = int(input("Enter number of lines triangle to have : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == j or i == (n+1-j)):
            print(i, end = '')
        else:
            print(' ', end = '')
    print()
    
# With Progressive number
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == j or i == (n+1-j)):
            print(j, end = '')
        else:
            print(' ', end = '')
    print()