''' 
Properties
Title: Two Sum
Level: easy

Statment:
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
'''

'''
Discussion of Solutions:

1. Brute Force Approach
- costly algorithm (inefficient)
- Check all possible pairs (i, j) where i != j
- Time Complexity: O(n²)
- Space Complexity: O(1)


2. Optimized Dictionary Approach
- Use a empty dictionary to store seen numbers and their indices
- for each number, check if (target - current) exists in the structure
- Time Complexity: O(n)
- Space Complexity: O(n)
'''



# Solutions
from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == target-nums[j]:
                    return [i, j]
        return [0, 0]


    def twoSum_version2(self, nums: List[int], target: int) -> List[int]:
        isHit = {  }

        for index, value in enumerate(nums):
            complement = target-value
            
            if complement in isHit:
                return [isHit[complement], index]

            isHit[value] = index

    def twoSum_version3(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i, num in enumerate(nums):
            A.append([num, i]) 
        
        A.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), 
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        
        return []




# Testing
solver = Solution()

# Solution 1
result = solver.twoSum1([3,4,5,6], 7)
print(f"nums = [3,4,5,6], target = 7, result = {result}")
# Output: [0,1]

result = solver.twoSum1([4,5,6], 10)
print(f"nums = [4,5,6], target = 10, result = {result}")
# Output: [0,2]

result = solver.twoSum1([5,5], 10)
print(f"nums = [5,5], target = 10, result = {result}")
# Output: [0,1]


# Solution 2