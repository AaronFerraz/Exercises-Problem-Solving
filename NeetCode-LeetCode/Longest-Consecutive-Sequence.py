''' 
Properties
Title: Longest Consecutive Sequence
Level: medium

Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
 
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
'''


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        prev = 0.2
        best = 1
        current = 1

        for i in nums:
            if i == prev:
                continue

            if i == prev + 1:
                current += 1
            else:
                current = 1
            
            if current > best: 
                best = current

            prev = i
        
        return best

    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:

            if (num-1) not in nums_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in nums_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


### Testes
solver = Solution()
test1 = solver.longestConsecutive([100,4,200,1,3,2])
print(f"Input: nums = [100,4,200,1,3,2] - Output: {test1}")  # Expected: 4  

test2 = solver.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(f"Input: nums = [0,3,7,2,5,8,4,6,0,1] - Output: {test2}")  # Expected: 9

test3 = solver.longestConsecutive2([1,0,1,2])
print(f"Input: nums = [1,0,1,2] - Output: {test3}")  # Expected: 3