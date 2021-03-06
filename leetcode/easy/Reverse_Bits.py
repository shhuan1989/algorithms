# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-11 20:20

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).



"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        return result




s = Solution()
for i in range(25):
    print('f({}) = {}'.format(i, s.reverseBits(i)))