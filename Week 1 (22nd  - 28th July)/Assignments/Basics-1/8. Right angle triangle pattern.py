# Write a program to display a pattern like a right angle triangle using an asterisk.

# The Pattern Like:

# *
# **
# ***
# ****

n = int(input("Enter number of lines triangle to have : "))
for i in range(n+1):  # Rangle is exclusive of last index
    print(i*'*')