# Description : 
# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. 
# Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
# He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

# Solution
def makeArrayConsecutive2(statues):
    
    statues = sorted(statues)
        
    return (statues[-1] - statues[0] + 1) - len(statues)
    
# Other solution
def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1
    
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
