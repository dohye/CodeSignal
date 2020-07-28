# Description :
"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
Given a string, find out if it satisfies the IPv4 address naming rules.
"""

# Solution :
def isIPv4Address(inputString):

    result = True
    if inputString.count('.') != 3:
        result = False
    
    else:
        a = inputString.split('.')    
        for i in a:
            try:
                if str(int(i)) == str(i):
                    i = int(i)
                    if 0 <= i <= 255: pass
                    else:
                        result = False

                else: result = False
                
            except:
                result = False
                
    return result
    
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
