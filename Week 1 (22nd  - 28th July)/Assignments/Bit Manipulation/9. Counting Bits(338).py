# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 
# Constraints: 0 <= n <= 105
 
# Follow up: It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

from typing import List


originalNum = input("Enter the number : ")
num = int(originalNum)

def countBits(n: int):
        lst = []

        for i in range (n+1):
            count = 0
            n = i
            while (n > 0):
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            lst.append(count)
        return lst
    
print(countBits(num))

def countBits1(n: int) -> List[int]:
        lst: List[int] = [0] * (n+1)

        for i in range (1,n+1):
            lst[i] = lst[i >> 1] + (i & 1)
        return lst
    
print(countBits1(num))