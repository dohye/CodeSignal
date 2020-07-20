# Description :
"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a strictly increasing sequence from the input
"""

# Solution :
def arrayChange(a):
    x = 0
    for i in range(len(a)-1):
        
        if a[i] >= a[i+1]:
            x += a[i] + 1 - a[i+1]
            a[i+1] = a[i] + 1
            
    return x
    
    
        
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
