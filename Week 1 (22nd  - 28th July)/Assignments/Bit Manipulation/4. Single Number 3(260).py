# 260. Single Number III
# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

#  Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

# Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]

# Example 3:
# Input: nums = [0,1]
# Output: [1,0]
 
# Constraints:
# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.

from collections import defaultdict
from typing import List


lst = list(map(int, input("Enter (Numbers)strings format : ").split()))
lstoutput: List[int] = []

def singleNumber(nums: List[int]) -> List[int]:
    count = defaultdict(int)
    for x in nums:
        count[x] += 1

    for x, freq in count.items():
        if freq == 1:
            lstoutput.append(x)

    return lstoutput

print(f"{singleNumber(lst)} is the list of numbers which appear only once")

def singleNumber31(nums: List[int]) -> List[int]:
    res = set()
    for num in nums:
        if num not in res:
            res.add(num)
        else:
            res.remove(num)
    return list(res)

print(f"{singleNumber31(lst)} is the list of numbers which appear only once")

def singleNumber32(nums: List[int]) -> List[int]:
    xor = 0
    # XOR all numbers to get the XOR of the two unique numbers
    for num in nums:
        xor ^= num

    # Get the rightmost set bit
    mask = xor & -xor

    num1 = num2 = 0
    # Partition the numbers into two groups and XOR each group
    for num in nums:
        if num & mask:
            num1 ^= num
        else:
            num2 ^= num
        
    return [num1, num2]

print(f"{singleNumber32(lst)} is the list of numbers which appear only once")


