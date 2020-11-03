# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/22

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    
    k, i, j = 0, 0, 1
    while k < N and i < N and j < N:
        if A[(i+k) % N] == A[(j+k) % N]:
            k += 1
        else:
            if A[(i+k) % N] > A[(j+k) % N]:
                i = i + k + 1
            else:
                j = j + k + 1
            if i == j:
                i += 1
            k = 0
    
    i = min(i, j)
    
    print(' '.join(map(str, A[i:] + A[:i])))
            