# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    L, N = map(int, input().split())
    
    tree = [2 for _ in range(L+1)]
    
    small = 0
    for i in range(N):
        a, b, c = map(int, input().split())
        if a == 0:
            for i in range(b, c+1):
                if tree[i] == 1:
                    small += 1
                tree[i] = 0
        else:
            for i in range(b, c+1):
                if tree[i] == 0:
                    tree[i] = 1
    
    print(len([v for v in tree if v == 1]))
    print(small)