# Description :
"""
Given array of integers, remove each kth element from it.
"""

# Solution :
def extractEachKth(inputArray, k):
    cnt = 0
    for i in range(len(inputArray)):        
        if (i+1) % k == 0:
            del inputArray[i-cnt] 
            cnt += 1
    return inputArray
    
# Other Solution:
def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray

# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
