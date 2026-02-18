'''
Title: Add Binary
Level: easy

Statement:
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''

from typing import List

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_binary = bin(int(a, 2) + int(b, 2))

        return sum_binary[2:]
    
    

### Testes
solver = Solution()

test1 = solver.addBinary("11", "1")
print(f"Input: a = '11', b = '1' - Output: {test1}")

test2 = solver.addBinary("1010", "1011")
print(f"Input: a = '1010', b = '1011' - Output: {test2}")
