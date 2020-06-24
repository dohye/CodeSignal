# Description :
# Given a sequence of integers as an array, 
# determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
 
# Note: 
# sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. 
# Sequence containing only one element is also considered to be strictly increasing.


# solution
def almostIncreasingSequence(sequence):
    
    if len(sequence) == 1:
        return True
    
    count = 0
    for i in range(len(sequence)-1):

        if sequence[i] >= sequence[i+1]:
            count += 1
            
            if count > 0 :
                s = sequence[:i] + sequence[i+1:]
                s2 = sequence[:(i+1)] + sequence[(i+2):]
                if s == sorted(list(set(s))) or s2 == sorted(list(set(s2))):
                    return True
                else:
                    return False


