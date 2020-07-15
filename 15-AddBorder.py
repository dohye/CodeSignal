# Description :
"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""

# Solution :
def addBorder(picture):
    
    out = ["*" * (max([len(i) for i in picture]) + 2)]
    for i in picture:
        out.append("*" + i + "*")
    out.append(out[0])
    
    return out
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
