# Write a program to display a pattern like a right angle triangle using an asterisk.

# The Pattern Like:

# *
# **
# ***
# ****

n = int(input("Enter number of lines triangle to have : "))
for i in range(n+1):  # Range is exclusive of last index
    print(i*'*')
    
for i in range(n+1):  # Range is exclusive of last index
    print(i*'* ')
    
# Left angled triangle
for i in range(n+1):
    s = ' ' * (n-i)
    print(s, end = '')
    s = '*' * i
    print(s)  

for i in range(n+1):
    s = '  ' * (n-i)
    print(s, end = '')
    s = '* ' * i
    print(s)  
    