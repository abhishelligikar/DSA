# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

from collections import defaultdict
from typing import List


lst = list(map(int, input("Enter (Numbers)strings format : ").split()))

def missingNumber(nums: List[int]) -> int:
    
    array = [-1] * (len(nums) + 1)
    
    for num in nums:
        array[num] = num
    
    for i in range(len(array)):
        if array[i] == -1:
            return i
        
    return 0

print(f"Missing number in {lst} is : '{missingNumber(lst)}'")

def missingNumber1(nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    for num in nums:
        ans ^= num
    return ans

print(f"Missing number in {lst} is : '{missingNumber1(lst)}'")

def missingNumber2(nums: List[int]) -> int:
    n = len(nums)
    Tsum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return Tsum - actual_sum

print(f"Missing number in {lst} is : '{missingNumber2(lst)}'")

def missingNumber3(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
        
    # Case 1
    if nums[0] != 0:
        return 0
        
    # Case 2
    if nums[-1] != n:
        return n
        
    # Case 3
    for i in range(1, len(nums)):
        if nums[i] != i:
            return i
        
    return 0

print(f"Missing number in {lst} is : '{missingNumber3(lst)}'")



    

