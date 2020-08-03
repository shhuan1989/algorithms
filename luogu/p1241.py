# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    s = input().strip()
    q = []
    ns = len(s)
    mark = [0 for _ in range(ns)]
    for i, ch in enumerate(s):
        if ch in {'(', '['}:
            q.append((i, ch))
        elif ch == ')':
            if q and q[-1][1] == '(':
                q.pop()
            else:
                mark[i] = 1
        else:
            if q and q[-1][1] == '[':
                q.pop()
            else:
                mark[i] = 1
    for i, ch in q:
        mark[i] = 1
    ans = []
    vmap = {
        '(': ')',
        '[': ']',
        ']': '[',
        ')': '('
    }
    for i, ch in enumerate(s):
        if mark[i] == 0:
            ans.append(ch)
        elif mark[i] == 1:
            if ch in {'(', '['}:
                ans.append(ch)
                ans.append(vmap[ch])
            else:
                ans.append(vmap[ch])
                ans.append(ch)
    print(''.join(ans))
    