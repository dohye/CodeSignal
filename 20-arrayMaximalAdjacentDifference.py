# Description :
"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
"""

# Solution :
def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i] - inputArray[i+1]) for i in range(len(inputArray)-1)])
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
