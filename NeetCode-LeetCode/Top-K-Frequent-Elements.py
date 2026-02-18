''' 
Properties
Title: Top K Frequent Elements
Level: Medium  

Statement: 
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_freq = sorted(freq_map.items(), key = lambda x: x[1])
        return [num for num, freq in sorted_freq[-k:]]



# Tests
solver = Solution()
print(f"nums = [1, 2, 2, 3, 3, 3], k = 2 - Output: {solver.topKFrequent([1,2,2,3,3,3], 2)}")  # Expected: [2,3]
print(f"nums = [7, 7], k = 1 - Output: {solver.topKFrequent([7,7], 1)}")  # Expected: [7]