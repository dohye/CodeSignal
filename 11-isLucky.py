# Description :

"""
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
"""

# Solution:

def isLucky(n):
    n = str(n)
    half = len(n) // 2
    
    first = 0
    second = 0
    for i in range(len(n)):
        if i < half:
            first += int(n[i])
        else:
            second += int(n[i])    
    
    return first == second
    
    
# Other solution

def isLucky(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
