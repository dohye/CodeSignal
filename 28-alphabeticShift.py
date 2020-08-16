# Description :
"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
i.e. replace a with b, replace b with c, etc (z would be replaced by a).
"""


# Solution :
def alphabeticShift(inputString):

    alphabet = [chr(x) for x in range(97,123)]
    
    shift_list = [alphabet[alphabet.index(s) + 1] if s != alphabet[-1] else 'a' for s in inputString]
        
    return ''.join(shift_list)
    
    
# Other Solution:
def alphabeticShift(inputString):
    return ''.join((chr(ord(i)+1) if i!="z" else "a" for i in inputString))

# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
