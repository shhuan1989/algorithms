# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/20

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
    
    ans = N
    while N >= K:
        ans += N // K
        N = N % K + (N // K)
        
    
    print(ans)