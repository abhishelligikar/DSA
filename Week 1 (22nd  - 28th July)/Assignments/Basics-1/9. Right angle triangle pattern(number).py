# Write a  program to display a pattern like a right angle triangle with a number.

# The Pattern Like:

# 1
# 12
# 123
# 1234

n = int(input("Enter number of lines triangle to have : "))
previous = ''
for i in range(1,n+1):  # Rangle is exclusive of last index
    previous += f"{i}"
    print(previous)