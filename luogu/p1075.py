# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List





if __name__ == '__main__':
    V = int(input())

    N = 10**5
    isprime = [True for _ in range(N)]
    for i in range(2, N+1):
        if not isprime:
            continue
        v = i + i
        while v < N:
            isprime[v] = False
            v += i
            
    for i in range(2, N):
        if V % i == 0:
            print(max(i, V//i))
            exit(0)
    
    