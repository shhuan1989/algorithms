# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':

    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    
    ans = 0
    k = 0
    for i, v in enumerate(A):
        if k + v > K:
            ans += 1
            k = 0
        k += v
    
    if k > 0:
        ans += 1
    
    print(ans)