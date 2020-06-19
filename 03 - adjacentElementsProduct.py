# Description
# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.


# solution
def adjacentElementsProduct(inputArray):
    
    out = list()
    
    for i in range(len(inputArray)):
        if i > 0 :
            prod = inputArray[i-1] * inputArray[i]
            out.append(prod)

    return max(out)


## solution - list comprehension
def adjacentElementsProduct(inputArray):
    
    return max([inputArray[i] * inputArray[i-1] for i in range(len(inputArray)) if i > 0])


# other solution
def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
