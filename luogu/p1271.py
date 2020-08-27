# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    wc = [0 for _ in range(1000)]
    for v in A:
        wc[v] += 1
    
    for w in range(1000):
        for i in range(wc[w]):
            print(w, end=' ')
    print()