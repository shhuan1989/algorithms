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

def gcd(x, y):
    while y:
        x, y = y, x%y
    
    return x

if __name__ == '__main__':

    N = int(input())
    ans = []
    for i in range(N):
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        ans.append('no' if gcd(abs(x1-x2), abs(y1-y2)) == 1 else 'yes')
        
    print('\n'.join(ans))