# Description :
"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
Check if the given string is a correct variable name.
"""

# Solution :
def variableName(name):

    if name[0].isdigit():
        return False
    
    else:
        
        a = all([type(i) == str for i in name])
        b = all([i.isalpha() or i.isdigit() or i == '_' for i in name])
    
        return all([a,b])
        
# Other Solution:
def variableName(name):
    return name.isidentifier()
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
