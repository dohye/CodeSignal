# Description :
"""
Given two cells on the standard chess board, determine whether they have the same color or not.
"""

# Solution :
def chessBoardCellColor(cell1, cell2):
    
    c1 = ord(cell1[0]) + int(cell1[1])
    c2 = ord(cell2[0]) + int(cell2[1])

    return (c1 % 2 == 0) == (c2 % 2 == 0)

# Other Solution:
def chessBoardCellColor(cell1, cell2):
    
    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1]))%2==0
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
