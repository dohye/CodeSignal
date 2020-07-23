  
# Description :
"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.
Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.
Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
"""

# Solution :
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft == friendsLeft and yourRight == friendsRight:
        return True
    elif yourLeft == friendsRight and yourRight == friendsLeft:
        return True
    else:
        return False
        
# Other Solution:
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}
    
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
