# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/7

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
    neg = N < 0
    N = abs(N)
    ans = 0
    while N > 0:
        ans *= 10
        ans += N % 10
        N //= 10
    
    print(ans if not neg else -ans)