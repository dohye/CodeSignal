# Description :
"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
"""

# Solution :
def arrayReplace(inputArray, elemToReplace, substitutionElem):
   
    ans = list()
    for i in inputArray:
        if i != elemToReplace:
            ans.append(i)
        else:
            ans.append(substitutionElem)
    
    return ans
    
### list comprehension if else
def arrayReplace(inputArray, elemToReplace, substitutionElem):
   
    return [i if i != elemToReplace else substitutionElem for i in inputArray]
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
