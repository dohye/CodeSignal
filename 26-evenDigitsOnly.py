# Description :
"""
Check if all digits of the given integer are even.
"""

# Solution :
def evenDigitsOnly(n):
    n = str(n)            
    return all([int(i) % 2 == 0 for i in n])
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
