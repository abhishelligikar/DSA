# Write a program to display a pattern like a triangle using an number.

# The Pattern Like:

# *   *
#  * *
#   *
#  * *
# *   *

n = int(input("Enter number of lines triangle to have : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == j or i == (n+1-j)):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
    