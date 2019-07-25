# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-07-19

"""

import collections
import time
import os
import sys
import bisect
import heapq

#!/bin/python

import math
import os
import random
import re
import sys


class SparseTable:
    """
    能查询区间和、最大最小值，更新比较慢
    """
    
    def __init__(self):
        self.st = [[0]]
        self.mst = [[0]]
        self.k = 0
    
    def build(self, A):
        n = len(A)
        m = int(math.ceil(math.log(n, 2))) + 1
        self.k = m
        
        # st[i, j] will store the answer for the range [i,i+2^j−1] of length 2^j
        st = [[0 for _ in range(m)] for _ in range(n)]
        mst = [[float('-inf') for _ in range(m)] for _ in range(n)]
        for i, v in enumerate(A):
            st[i][0] = v
            mst[i][0] = v
        
        for j in range(1, m):
            for i in range(n - (1 << j) + 1):
                st[i][j] = st[i][j - 1] + st[i + (1 << (j - 1))][j - 1]
                mst[i][j] = max(mst[i][j - 1], mst[i + (1 << (j - 1))][j - 1])
        self.st = st
        self.mst = mst
    
    def sum(self, l, r):
        ans = 0
        for j in range(self.k, -1, -1):
            if r - l + 1 >= 1 << j:
                ans += self.st[l][j]
                l += 1 << j
        return ans
    
    def max(self, l, r):
        ans = float('-inf')
        for j in range(self.k, -1, -1):
            if r - l + 1 >= 1 << j:
                ans = max(ans, self.mst[l][j])
                l += 1 << j
        return ans
    
    def update(self, pos, value):
        pass
            
# Complete the serviceLane function below.
def serviceLane(n, width, cases):
    s = SparseTable()
    s.build([-v for v in width])
    return [abs(s.max(l, r)) for l, r in cases]



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, width, cases)

    print('\n'.join(map(str, result)))
