# 231. Power of Two : Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 2**0 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 2**4 = 16

# Example 3:
# Input: n = 3
# Output: false

# Constraints:
# -231 <= n <= 231 - 1
 
# Follow up: Could you solve it without loops/recursion?

import math


number_to_check = int(input("Enter number to check for Odd or evenpower of 2 : "))

def isPowerOfTwo(n: int) -> bool:
    for i in range(31):
        ans = 2 ** i
        if ans == n:
            return True
    return False

print(f"{number_to_check} is a power of 2" if isPowerOfTwo(number_to_check) else f"{number_to_check} is not a power of 2")

def isPowerOfTwo1(n: int) -> bool:
    if n == 0:
        return False
        
    while n > 0:
        if n == 1:
            return True
        if n % 2 != 0:
            break
        n //= 2
    return False

print(f"{number_to_check} is a power of 2" if isPowerOfTwo1(number_to_check) else f"{number_to_check} is not a power of 2")

def isPowerOfTwo2(n: int) -> bool:
    x = 1
    while x <= n:
        if x == n:
            return True
        if x > 2 ** 30:
            break
        x = x << 1
    return False

print(f"{number_to_check} is a power of 2" if isPowerOfTwo2(number_to_check) else f"{number_to_check} is not a power of 2")

def isPowerOfTwo4(n: int) -> bool:
    if n == 0:
        return False
    return math.floor(math.log2(n)) == math.ceil(math.log2(n))

print(f"{number_to_check} is a power of 2" if isPowerOfTwo4(number_to_check) else f"{number_to_check} is not a power of 2")

def isPowerOfTwo5(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

print(f"{number_to_check} is a power of 2" if isPowerOfTwo5(number_to_check) else f"{number_to_check} is not a power of 2")

def isPowerOfTwo6(n: int) -> bool:
    if n <= 0:
        return False
    cnt = bin(n).count('1')
    return cnt == 1

print(f"{number_to_check} is a power of 2" if isPowerOfTwo6(number_to_check) else f"{number_to_check} is not a power of 2")

def isPowerOfTwo7(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    return (n % 2 == 0) and isPowerOfTwo7(n // 2)

print(f"{number_to_check} is a power of 2" if isPowerOfTwo7(number_to_check) else f"{number_to_check} is not a power of 2")