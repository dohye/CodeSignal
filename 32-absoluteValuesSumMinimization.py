# Description :
"""
You have deposited a specific amount of money into your bank account. 
Each year your balance increases at the same growth rate. 
With the assumption that you don't make any additional deposits, 
find out how long it would take for your balance to pass a specific threshold.
"""

# Solution :
def absoluteValuesSumMinimization(a):
    a_min = list()    
    for i in a:
        a_abs = 0
        for j in range(len(a)):
            a_abs += abs(a[j] - i)
        a_min.append(a_abs)

    x_idx = a_min.index(min(a_min))
    
    return a[x_idx]    
        
# Other Solution:
def absoluteValuesSumMinimization(A):

    return A[(len(A)-1)//2]

# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
