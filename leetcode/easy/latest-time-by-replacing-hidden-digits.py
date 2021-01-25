# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/24
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def maximumTime(self, x: str) -> str:
        y = list(x)
        if y[0] == '?':
            if y[1] == '?':
                y[0] = '2'
                y[1] = '3'
            elif int(y[1]) <= 3:
                y[0] = '2'
            else:
                y[0] = '1'
        if y[1] == '?':
            if y[0] == '2':
                y[1] = '3'
            else:
                y[1] = '9'
        if y[3] == '?':
            y[3] = '5'
        if y[4] == '?':
            y[4] = '9'
        
        return ''.join(y)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumTime('2?:?0'))
    print(s.maximumTime('0?:3?'))
    print(s.maximumTime('1?:22'))