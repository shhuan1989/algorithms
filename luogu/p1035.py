# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    K = int(input())
    
    s = [1.0]
    MAXN = 2000000
    for v in range(2, MAXN):
        s.append(s[-1] + 1/v)
    # print(s[:10])
    print(1 + bisect.bisect_right(s, K))