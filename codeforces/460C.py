# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/13/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, W, A):
    def check(val):
        """
        To check how many operations need to make all values of A greater or equal given value {val};
        Each operation will increase one segment [i, i+W-1] by one;
        Naive code will like
        
        for i in range(N):
            if A[i] < val:
                increase segment [i: i+W] by (val-A[i]), needs (val-A[i]) operations
        
        time complexity will be O(N*W);
        
        Here we can use open/close segment to make it O(N):
        
        curr is a variable to record the current added value
        A array to record the close value, for each i we add a {val}, we minus {val} at i+W
        for each i:
            current value should be A[i] + curr
            if A[i] + curr < val:
                let v = val-(A[i]+curr)
                add v to segment [i: i+W]
                minus curr with v at i+W
        
        :param val:
        :return:
        """
        needs = [val-v for v in A]
        delta = [0 for _ in range(N)]
        water = 0
        i = 0
        curr = 0
        while i < N:
            curr += delta[i]
            if needs[i] > curr:
                w = needs[i] - curr
                water += w
                curr += w
                if i + W < N:
                    delta[i + W] -= w
                if water > M:
                    return False
            i += 1
        return water <= M
    
    lo, hi = min(A), max(A) + M
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            lo = m + 1
        else:
            hi = m - 1
            
    return hi


N, M, W = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, M, W, A))