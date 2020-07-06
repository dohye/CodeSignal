# Description :

"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

ex)
For a = [-1, 150, 190, 170, -1, -1, 160, 180], 
the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""

# Solution:

def sortByHeight(a):
            
    tree = -1
    sort_list = sorted([num for num in a if num is not tree])
    result = [0 for i in range(len(a))]
    
    s = 0
    for i in range(len(a)):
        if a[i] == tree:
            result[i] = tree
    
        else:
            s += 1
            result[i] = sort_list[s-1]
            
    return result
    
    
# Other solution

def sortByHeight(a):

    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l

    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/

