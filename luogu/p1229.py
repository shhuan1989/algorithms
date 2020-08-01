# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/29 20:57

"""



if __name__ == '__main__':
    # sys.stdin = open('p1229_6.in', 'r')
    S = input().strip()
    T = input().strip()



    def dfs(s, t):
        if not s or len(s) == 1:
            return 1

        if s[0] != t[-1]:
            return 0

        wca = collections.defaultdict(int)
        wcb = collections.defaultdict(int)
        ans = 0
        for i in range(1, len(s)):
            a, b = s[i], t[i-1]
            wca[a] += 1
            wcb[b] += 1
            if wca == wcb:
                ans += dfs(s[1:i+1], t[:i]) * dfs(s[i+1:], t[i:-1]) * (1 if i < len(s)-1 else 2)

        # print(s, t, ans)
        return ans

    print(dfs(S, T))