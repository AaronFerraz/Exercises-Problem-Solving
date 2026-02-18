''' 
Properties
Title: Length Of Last Word
Level: easy

Statement:
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
 
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

'''
Discussion of Solutions:
1. One-Pass Approach (or Using built-ins)
- firstly, leading/trailing whitespace is removed using strip()
- then, the string is split into a list of words using split(). This automatically handles multiple spaces between words.
- the code checks if the resulting list is empty
- if not empty, it returns the length of the last word in the list
- Time Complexity: O(n)
- Space Complexity: O(n)

2. Optimized Approach: Reverse Iteration (Constant Space)
- This solution iterates through the string from right to left, avoiding the creation of an intermediate list of words.
- It first skips any trailing spaces by moving an index `i` backward until a non-space character is found.
- Then, it counts backward from that non-space character, incrementing a `length` counter, until it encounters a space or reaches the beginning of the string.
- This approach directly calculates the length of the last word without storing all words.
- Time Complexity: O(n)
- Space Complexity: O(1)
'''


# Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:  
        words = s.strip().split(" ")

        if not words:
            return 0
        
        return len(words[-1]) 
    
    def lengthOfLastWord_version2(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length



### Tests
Solver = Solution()

print(f"A saída é: {Solver.lengthOfLastWord("Olá mundo")}")
print(f"A saída é - versão 2: {Solver.lengthOfLastWord_version2("Olá mundo")}") # Output expected: 5

print(f"A saída é: {Solver.lengthOfLastWord("fly to the moon")}")
print(f"A saída é - versão 2: {Solver.lengthOfLastWord_version2("fly to the moon")}") # Output expected: 4

print(f"A saída é: {Solver.lengthOfLastWord("encontrei um paralelepipedo")}")
print(f"A saída é - versão 2: {Solver.lengthOfLastWord_version2("encontrei um paralelepidedo")}") # Output expected: 14

print(f"A saída é: {Solver.lengthOfLastWord(" ")}")
print(f"A saída é - versão 2: {Solver.lengthOfLastWord_version2(" ")}") # Output expected: 0