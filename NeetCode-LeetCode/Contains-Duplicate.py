'''
Title: Contains Duplicate
Level: easy

Statement:
Given an integer array nums, return true if any value appears more 
than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
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
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

    def hasDuplicate3(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


### Testes
solver = Solution()

test1 = solver.hasDuplicate1([1, 2, 3, 3])
print(f"Input: nums = [1, 2, 3, 3] - Output: {test1}")

test2 = solver.hasDuplicate1([1, 2, 3, 4])
print(f"Input: nums = [1, 2, 3, 4] - Output: {test2}")

test3 = solver.hasDuplicate2([1, 2, 3, 4])
print(f"Input: nums = [1, 2, 3, 4] - Output: {test3}")

test4 = solver.hasDuplicate3([1, 2, 3, 4])
print(f"Input: nums = [1, 2, 3, 4] - Output: {test4}")
