# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

from typing import List


lst = list(map(int, input("Enter two (Numbers)strings in binary format : ").split()))

def singleNumber(nums: List[int]) -> int:
    nonRepetativeNumber = 0
    for i in range(len(nums)):
        nonRepetativeNumber ^= nums[i]
    return nonRepetativeNumber

print(f"Non Repetative number from list {lst} is {singleNumber(lst)}")