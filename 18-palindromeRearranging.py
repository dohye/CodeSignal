# Description :
"""
Given a string, find out if its characters can be rearranged to form a palindrome.
"""

# Solution :
def palindromeRearranging(inputString):
    
    d = dict()
    for key in set(inputString):
        d[key] = 0

    for key in inputString:
        d[key] += 1

    bool_list = [True if i%2==0 else False for i in d.values()]
    
    cnt = 0
    for i in bool_list:
        if i == False:
            cnt += 1
            
    return cnt == 0 or cnt == 1

# Other Solution:
def palindromeRearranging(inputString):

    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1
    
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
