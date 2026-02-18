''' 
Properties
Title: Group Anagrams
Level: Medium

Statement:
Given an array of strings strs, group all anagrams together into sublists. You may 
return the output in any order. An anagram is a string that contains the exact 
same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
'''


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = [word]
            else:
                anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


# Tests
solver = Solution()

print(f"Input: strs = [\"act\",\"pots\",\"tops\",\"cat\",\"stop\",\"hat\"] - Output: {solver.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])}") # Expected: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(f"Input: strs = [\"x\"] - Output: {solver.groupAnagrams(["x"])}") # Expected: [["x"]]
print(f"Input: strs = [\"\"] - Output: {solver.groupAnagrams([""])}") # Expected: [[""]]