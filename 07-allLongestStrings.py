# Description :
# Given an array of strings, return another array containing all of its longest strings.


#solution
def allLongestStrings(inputArray):
    
    max_len = max(len(arr) for arr in inputArray)
    
    return [arr for arr in inputArray if len(arr) == max_len]
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
