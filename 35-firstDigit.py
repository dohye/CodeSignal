# Description :
"""
Find the leftmost digit that occurs in a given string.
"""

# Solution :
def firstDigit(inputString):
    res = []
    for char in inputString:
        try:
            ans = int(char)
            res.append(str(ans))
        except:
            pass
    return res[0]
    
# Other Solution:
def firstDigit(inputString):
    for i in inputString:
        if i.isdigit():
            return i

# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
