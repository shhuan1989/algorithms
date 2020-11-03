# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    a, b = map(int, input().split())
    
    ans = 0
    for v in range(a, b+1):
        if v % 2 == 1 or v % 4 == 0:
            ans += 1
    print(ans)