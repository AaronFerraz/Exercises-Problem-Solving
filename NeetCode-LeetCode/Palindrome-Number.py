''' 
Properties
Title: Palindrome Number
Level: easy

Statement:
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 
121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

'''
Discussion of Solutions:
1. String Slicing
Firstly, the integer x is converted to its string representation using str(x).
Then, a reversed version of this string is created using Python's extended slice notation [::-1].
Finally, the original string representation is directly compared to its reversed version. If they are identical, the integer is a palindrome.
Time Complexity: O(n), where n is the number of digits in the integer. String conversion takes O(n) time. Creating the reversed string slice also takes O(n) time. The comparison between the two strings takes O(n) time.
Space Complexity: O(n). The conversion to a string creates a new string of length n. The slicing [::-1] creates another new string of length n (the reversed version). Therefore, the space required is proportional to the number of digits.

2. Manual String Reversal
Firstly, the integer is converted to its string representation (text).
Then, the code iterates through the text string character by character.
Inside the loop, each character is prepended to a new string reserve, effectively building the reversed string.
Finally, the original string text is compared to the manually reversed string reserve.
Time Complexity: O(n), where n is the number of digits (due to string conversion, loop, and comparison).
Space Complexity: O(n), as both the initial string and the reversed string require space proportional to n.

3. Two Pointers
Firstly, the integer is converted to its string representation (text).
Then, two index pointers, left and right, are initialized at the beginning and end of the text string, respectively.
The code enters a loop that continues as long as left is less than right.
Inside the loop, it compares the characters at the left and right indices. If they don't match, the function immediately returns False.
If the characters match, the left pointer is incremented, and the right pointer is decremented, moving them closer to the center.
If the loop completes without finding any mismatches, it means the string is a palindrome, and the function returns True.
Time Complexity: O(n), where n is the number of digits (due to string conversion and the loop running approximately n/2 times).
Space Complexity: O(n), primarily due to the initial string conversion. The comparison phase itself uses only O(1) extra space for the pointers.
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    def isPalindrome_manualform(self, x: int) -> bool:
        text = str(x)
        reserve = ""
        for char in text:
            reserve = char + reserve
        return text == reserve
    
    def isPalindrome_version3(self, x: int) -> bool:
        text = str(x)
        left, right = 0, len(text) - 1

        while right > left:
            if text[right] != text[left]:
                return False
            left += 1
            right -= 1
        
        return True



### Tests
Solver = Solution()

print(f"Output version 1 - 10101: {Solver.isPalindrome(10101)}")
print(f"Output version 2 - 10101: {Solver.isPalindrome_manualform(10101)}")
print(f"Output version 3 - 10101: {Solver.isPalindrome_version3(10101)}")

print(f"Output version 1 - 11010: {Solver.isPalindrome(11010)}")
print(f"Output version 2 - 11010: {Solver.isPalindrome_manualform(11010)}")
print(f"Output version 3 - 11010: {Solver.isPalindrome_version3(11010)}")
