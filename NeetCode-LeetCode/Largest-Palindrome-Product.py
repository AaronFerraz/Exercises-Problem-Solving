''' 
Properties
Title: Largest Palindrome Product
Level: Problem 4 - Project Euler

Statement: 
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two -digit numbers is   .

Find the largest palindrome made from the product of two -digit numbers.
'''

import math

class Solution:
    def largestPalindromeThreeDigits(self):
        max_palindromic = 0

        for i in range(999, 99, -1):
        
            if i * i < max_palindromic:
                break
                
            for j in range(i, 99, -1):
                product = i * j

                if product <= max_palindromic:
                    break
                s_product = str(product)
                
                if s_product == s_product[::-1]:
                    max_palindromic = product

        return max_palindromic
    

#Tests
solver = Solution()
print(f"O maior palíndromo produto de dois numeros de 3 dígitos é: {solver.largestPalindromeThreeDigits()}")