# 1929. Concatenation of Array

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
 
# Constraints:
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000


from typing import List
original_lst = list(map(int, input("Enter (Numbers)strings : ").split()))
lst = original_lst
def getConcatenation(nums: List[int]) -> List[int]:
    return nums + nums

print(f"Concatenated array output would be {getConcatenation(lst)}")

lst = original_lst
def getConcatenation1(nums: List[int]) -> List[int]:
    return nums * 2

print(f"Concatenated array output would be {getConcatenation1(lst)}")

lst = original_lst
def getConcatenation2(nums: List[int]) -> List[int]:
        ans = []
        for i in range (2):
            for j in nums:
                ans.append(j)
        return ans
    
print(f"Concatenated array output would be {getConcatenation2(lst)}")

lst = original_lst  
def getConcatenation3(nums: List[int]) -> List[int]:
    nums.extend(nums)
    return nums

print(f"Concatenated array output would be {getConcatenation3(lst)}")

lst = original_lst
def getConcatenation4(nums: List[int]) -> List[int]:
    length = len(nums)
    ans = [0] * length * 2
    for i in range(length):
        ans[i] = nums[i]
        ans[length+i] = nums[i]
    return ans

print(f"Concatenated array output would be {getConcatenation4(lst)}")