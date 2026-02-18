'''
Properties
Title: Valid Anagram
Level: easy

Statement:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"

Output: false
Constraints:
s and t consist of lowercase English letters.
'''

'''
Discussion of Solutions:
1. Sorting
Approach: This method first checks if the lengths of the two strings s and t are 
different. If they are, the strings cannot be anagrams, and it returns False. 
If the lengths are the same, it sorts the characters of both strings alphabetically 
using the built-in sorted() function. If the resulting sorted lists of characters are identical, 
it means the original strings contained the same characters with the same frequencies, thus they are anagrams.
Time Complexity: O(n log n), where n is the length of the strings. The dominant 
operation is sorting. Python's sorted() function typically uses Timsort, which has an average 
and worst-case time complexity of O(n log n). The initial length check is O(1), and the final 
list comparison is O(n).
Space Complexity: O(n). The sorted() function usually creates new lists to store 
the sorted characters, requiring space proportional to the length of the strings.

2. Frequency Counter (Hash Map)
Approach: This method also starts with a length check, returning False if len(s) 
differs from len(t). It then initializes two hash maps (dictionaries in Python), 
countS and countT, to store the frequency of each character in strings s and t, 
respectively. It iterates through the strings once, incrementing the count for 
each character in its corresponding dictionary. The dict.get(key, 0) method efficiently 
handles cases where a character is encountered for the first time. Finally, it compares 
the two frequency maps. If the maps are identical (meaning every character appears the 
same number of times in both strings), the strings are anagrams.
Time Complexity: O(n). The initial length check is O(1). The loop iterates n times. 
Dictionary insertions and lookups (get and [] =) take O(1) time on average. 
Comparing the two dictionaries takes O(k) time in the best/average case, where 
k is the number of unique characters (at most n, often much smaller, e.g., 26 
for lowercase English letters). Thus, the overall complexity is dominated by the 
loop, making it O(n).
Space Complexity: O(k) or O(n). Space is required to store the two hash maps. 
In the worst case, if all characters are unique, the space needed is proportional 
to the length of the strings, O(n). However, if the character set is bounded 
(e.g., ASCII or lowercase English letters), the space complexity is O(1) because 
the size of the dictionaries is limited by the size of the character set (e.g., 26 or 128).
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    

    def isAnagram_version2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT



# Tests
Solver = Solution()

print(f"Input 1 (version 1) - 'racecar' and 'carrace' result {Solver.isAnagram("racecar", "carrace")}")
print(f"Input 1 (version 2) - 'racecar' and 'carrace' result {Solver.isAnagram("racecar", "carrace")}")

print(f"Input 2 (version 1) - 'jar' and 'jam' result {Solver.isAnagram("jar", "jam")}")
print(f"Input 2 (version 2) - 'jar' and 'jam' result {Solver.isAnagram("jar", "jam")}")
