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
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        
        cc = collections.Counter(answers)
        res = 0
        
        for k, v in cc.items():
            if k + 1 >= v:
                res += k + 1
            else:
                
                if v % (k+1) == 0:
                    res += v
                else:
                    res += (v // (k + 1) + 1) * (k+1)
                    
        return res