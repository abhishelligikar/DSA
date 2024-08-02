# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 
# Constraints: 
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

str1, str2 = map(str, input("Enter two (Numbers)strings in binary format seaparted by - ").split(","))

def addBinary(a: str, b: str) -> str:
    s = ""
    carry = 0
    i = len(str1) - 1
    j = len(str2) - 1
    
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
            
        if j >= 0:
            carry += int(b[j])
            j -= 1
            
        s = str(carry % 2) + s
        carry //= 2
        
    return s

print(f"Binary Addition of {str1} and {str2} is '{addBinary(str1, str2)}'")

def addBinary1(a: str, b: str) -> str:
    x=int(a,2)
    y=int(b,2)
    z=x+y
    z=bin(z)[2:]
    return z

print(f"Binary Addition of {str1} and {str2} is '{addBinary1(str1, str2)}'")