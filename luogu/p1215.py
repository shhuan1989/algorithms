# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    ABC = [A, B, C]
    
    vis = set()
    def dfs(abc):
        for i in range(3):
            for j in range(3):
                if i != j:
                    # i => j
                    k = min(abc[i], ABC[j]-abc[j])
                    nabc = abc.copy()
                    nabc[i] = abc[i]-k
                    nabc[j] = abc[j]+k
                    s = '-'.join(map(str, nabc))
                    if s not in vis:
                        vis.add(s)
                        dfs(nabc)
    dfs([0, 0, C])
    ans = []
    for s in vis:
        abc = [int(x) for x in s.split('-')]
        if abc[0] == 0:
            ans.append(abc[-1])
    # print(vis)
    print(' '.join(map(str, list(sorted(ans)))))