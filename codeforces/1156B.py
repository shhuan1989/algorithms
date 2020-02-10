# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/15/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def dfs(chs, perm):
    if not chs:
        return perm
    
    for v in chs:
        if not perm or abs(ord(v) - ord(perm[-1])) > 1:
            a = dfs(chs - {v}, perm + [v])
            if a:
                return a
    return []


def rearrange(s):
    wc = collections.Counter(s)
    chs = set(wc.keys())
    p = dfs(chs, [])
    if p:
        ans = ''
        for v in p:
            ans += v * wc[v]
        return ans
    
    return 'No answer'


N = int(input())
ans = []
for i in range(N):
    s = input()
    ans.append(rearrange(s))
print('\n'.join(ans))