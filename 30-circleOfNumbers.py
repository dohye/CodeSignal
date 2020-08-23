  
# Description :
"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal 
(note that 0 and n - 1 are neighboring, too).
Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
"""

# Solution :
def circleOfNumbers(n, firstNumber):
    ans = firstNumber + (n // 2)
    if ans >= n:
        ans = ans - n
        
    return ans
        
# Other Solution:
def circleOfNumbers(n, firstNumber):

    return (firstNumber + (n // 2))%n
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
