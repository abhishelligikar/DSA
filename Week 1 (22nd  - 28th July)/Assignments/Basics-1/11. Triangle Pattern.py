# Write a program to display a pattern like a triangle using an asterisk.

# The Pattern Like:

#    *
#   * *
#  * * *
# * * * *

n = int(input("Enter number of lines triangle to have : "))
for i in range(1, n+1):
    s = ' ' * (n-i)
    print(s, end = '')
    s = '* ' * i
    print(s)    