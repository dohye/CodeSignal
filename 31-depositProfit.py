# Description :
"""
You have deposited a specific amount of money into your bank account. 
Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, 
find out how long it would take for your balance to pass a specific threshold.
"""

# Solution :
def depositProfit(deposit, rate, threshold):
    
    year = 0
    
    while threshold > deposit:
        money = (rate * deposit / 100) + deposit
        deposit = money
        year += 1
        
    return year
        
# Other Solution:
def depositProfit(deposit, rate, threshold):

    return math.ceil(math.log(threshold/deposit, 1+rate/100))
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
