# Description
# Given two strings, find the number of common characters between them.
# For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3.
# Strings have 3 common characters - 2 "a"s and 1 "c".

# Solution
def commonCharacterCount(s1, s2):
    return sum([min(s1.count(i), s2.count(i)) for i in set(s1)])

# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
