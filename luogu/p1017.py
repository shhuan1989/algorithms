# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

Z = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']

def solve(N, M):
    ans = ''
    while N != 0:
        K = N % M
        N //= M
        if K < 0:
            K -= M
            N += 1
        ans += Z[K]
    
    return ans[::-1]
        


if __name__ == '__main__':
    N, M = map(int, input().split())
    print('{}={}(base{})'.format(N, solve(N, M), M))
    