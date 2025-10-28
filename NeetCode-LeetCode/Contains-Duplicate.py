'''
Title: Contains Duplicate
Level: easy

Statment:
Given an integer array nums, return true if any value appears more 
than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
'''

'''

'''

from typing import List

class Solution:

    def hasDuplicate1(self, nums: List[int]) -> bool:
        aux_list = []

        for i in nums:
            if i in aux_list:
                return True

            aux_list.append(i)
        
        return False
    
    def hasDuplicate2(self, nums: List[int]) -> bool:
        for i in nums:
            for j in nums:
                if(nums.index(i)):
                    ...
                return True

            aux_list.append(i)
        
        return False


solver = Solution()

# Solution 1
test1 = solver.hasDuplicate1([1, 2, 3, 3])
print(f"Input: nums = [1, 2, 3, 3] - Output: {test1}")

test2 = solver.hasDuplicate1([1, 2, 3, 4])
print(f"Input: nums = [1, 2, 3, 4] - Output: {test2}")
