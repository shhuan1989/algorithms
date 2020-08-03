# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/28

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
    A = [(v, i+1) for i, v in enumerate(A)]
    A.sort()
    
    wait = [0]
    t = A[0][0]
    for i in range(1, N):
        wait.append(t)
        t += A[i][0]
    
    avgw = sum(wait) / len(wait)
    
    print(' '.join(map(str, [i for v, i in A])))
    print('{:.2f}'.format(avgw))