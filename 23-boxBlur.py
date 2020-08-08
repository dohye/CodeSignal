# Description :
"""
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! 
You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.
The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way
: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. 
All the pixels on the border of x are then removed.
Return the blurred image as an integer, with the fractions rounded down.
"""

# Solution :
def boxBlur(image):
    r = len(image)
    c = len(image[0])
    
    ans = list()
    for i in range(1, r - 1):
        square = list()
        for j in range(1, c - 1):
            sum_ = sum(image[i - 1][j - 1: j + 2] + image[i][j - 1: j + 2] + image[i + 1][j - 1: j + 2])
            square.append(int(sum_ / 9))
        ans.append(square)
    return ans
    
        
# [Copyright © 2020 BrainFights, Inc. All rights reserved.]
# https://codesignal.com/
