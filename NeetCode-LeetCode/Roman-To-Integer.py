''' 
Properties
Title: Palindrome Number
Level: easy   

Statement: 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written 
as IV. Because the one is before the five we subtract it making four. The same 
principle applies to the number nine, which is written as IX. There are six 
instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
- Given a roman numeral, convert it to an integer.

 
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_map[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value
        
        return total
    
    def romanToInt2(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        translation = {
            'IV': 'IIII',
            'IX': 'VIIII',
            'XL': 'XXXX',
            'XC': 'LXXXX',
            'CD': 'CCCC',
            'CM': "DCCCC"
        }

        for old, new in translation.items():
            s = s.replace(old, new)
  
        return sum(roman_map[char] for char in s)
    


### Testes
solver = Solution()

print(f"Teste 1 - Número: XXI -> resultado: {solver.romanToInt('XXI')}")
print(f"Teste 2 - Número: III -> resultado: {solver.romanToInt('III')}")
print(f"Teste 3 - Número: LVIII -> resultado: {solver.romanToInt('LVIII')}")
print(f"Teste 4 - Número: MCMXCIV -> resultado: {solver.romanToInt('MCMXCIV')}")

print(f"Teste 5 - Número: MCMXCIV -> resultado: {solver.romanToInt2('MCMXCIV')}")
