# 137. Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

#  Example 1:
# Input: nums = [2,2,3,2]
# Output: 3

# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.

from collections import defaultdict
from typing import List


lst = list(map(int, input("Enter two (Numbers)strings in binary format : ").split()))

def singleNumber2(nums: List[int]) -> int:
    count = defaultdict(int)
    
    for x in nums:
        count[x] += 1
        
    for x, freq in count.items():
        if freq == 1:
            return x
        
    return x

print(f"Non Repetative number from list {lst} is {singleNumber2(lst)}")

def singleNumber22(nums: List[int]) -> int:
    for i in range(len(nums)):
        j = 0
        while j < len(nums):
            if nums[i] == nums[j] and i != j:
                break
            j += 1
        if j == len(nums):
            return nums[i]
    return -1  # This line should never be reached as per problem constraints

print(f"Non Repetative number from list {lst} is {singleNumber22(lst)}")

def singleNumber23(nums: List[int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & (~twos)
        twos = (twos ^ num) & (~ones)
        
    return ones

print(f"Non Repetative number from list {lst} is {singleNumber23(lst)}")
