# Write a program  to make such a pattern like a right angle triangle with a number which will repeat a number in a row.

# The Pattern Like:

#  1
#  22
#  333
#  4444

n = int(input("Enter number of lines triangle to have : "))
for i in range(1,n+1):  # Rangle is exclusive of last index
    print(i * f"{i}")