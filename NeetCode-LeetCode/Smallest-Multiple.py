''' 
Properties
Title: Smallest Multiple
Level: Problem 5 - Project Euler

Statement: 
2520 is the smallest number that can be divided by each of the numbers from  
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
'''

import math

class Solution:
    def mmc(self, a, b):
        return (a * b) // math.gcd(a,b)
    
    def smallestMultiple(self, n: int) -> int:
        resultado = 1
        for i in range(1, n + 1):
            resultado = self.mmc(resultado, i)
        return resultado
    

#Tests
solver = Solution()
print(f"Menor multiplo que pode ser dividido de 1 a 20: {solver.smallestMultiple(20)}")