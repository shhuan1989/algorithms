# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


MOD = 998244353

if __name__ == '__main__':
    n, m, l, r = map(int, input().split())
    if n * m % 2 == 1:
        print(pow(r - l + 1, n * m, MOD))
    else:
        e = r // 2 - (l - 1) // 2
        o = (r - l + 1) - e
        print((pow(e + o, n * m, MOD) + pow(e - o, n * m, MOD)) * (MOD + 1) // 2 % MOD)
