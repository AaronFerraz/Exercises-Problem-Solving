'''
Title: Longest Common Prefix
Level: easy

Statement:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    


### Testes
solver = Solution()

test1 = solver.longestCommonPrefix(["flower","flow","flight"])
print(f"Input: strs = ['flower','flow','flight'] - Output: {test1}")

test2 = solver.longestCommonPrefix(["dog","racecar","car"])
print(f"Input: strs = ['dog','racecar','car'] - Output: {test2}")