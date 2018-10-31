# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/11/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        if len(hand) % W != 0:
            return False
            
        cc = collections.Counter(hand)
        
        while cc:
            start = min(cc.keys())
            count = cc[start]
            
            for v in range(start, start+W):
                if v not in cc:
                    return False
                cc[v] -= count
                if cc[v] <= 0:
                    del cc[v]
        
        return True
        
        
s = Solution()
print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(s.isNStraightHand([1, 2, 3, 4, 5], 4))
