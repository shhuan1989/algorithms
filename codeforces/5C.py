# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/6/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(s):
    c = 0
    ans, tmp, count = 0, 0, 0
    for i, v in enumerate(s):
        if v == '(':
            c += 1
        else:
            c -= 1
            if c >= 0:
                tmp += 1
            else:
                if tmp > ans:
                    ans = tmp
                    count = 1
                elif tmp > 0 and tmp == ans:
                    count += 1
                tmp = 0
                c = 0
    if c == 0:
        if tmp > ans:
            ans = tmp
            count = 1
        elif tmp > 0 and tmp == ans:
            count += 1
            
    return ans * 2, max(count, 1)
    
            
    
s = input()
a, b = solve(s)
c, d = solve(['(' if v ==')' else ')' for v in s[::-1]])
if a > c or (a == c and b >= d):
    print('{} {}'.format(a, b))
else:
    print('{} {}'.format(c, d))