# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        if len(bits) == 1:
            return True


        if bits[-2:] == [0, 0]:
            return True


        def check(bits, index):
            if index == len(bits):
                return True
            elif index > len(bits):
                return False

            if bits[index] == 0:
                return check(bits, index+1)

            return check(bits, index+2)

        if check(bits[:-2], 0):
            return False

        return True

s = Solution()
print(s.isOneBitCharacter([1, 0, 0]))
print(s.isOneBitCharacter([1, 1, 1, 0]))