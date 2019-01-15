# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/18

"""

import collections
import time
import os
import sys
import bisect
import heapq


S = input()
N = len(S)

l, r = 0, N-1

ans = []
while l < r:
    if N % 2 != 0:
        ans.append(S[l])
        ans.append(S[r])
    else:
        ans.append(S[r])
        ans.append(S[l])
    l += 1
    r -= 1

if l == r:
    ans.append(S[l])

print(''.join(list(reversed(ans))))
