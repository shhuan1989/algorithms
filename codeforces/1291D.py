# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/3/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(s, queries):
    N = len(s)
    charcount = [[0 for _ in range(N+1)] for _ in range(26)]
    
    for i, v in enumerate(s):
        for ch in range(26):
            charcount[ch][i+1] = charcount[ch][i]
        ch = ord(v) - ord('a')
        charcount[ch][i+1] += 1
        
    # for i in range(26):
    #     print(charcount[i])
    
    ans = []
    for l, r in queries:
        if l == r:
            ans.append(True)
        elif s[l] != s[r]:
            ans.append(True)
        else:
            c = 0
            for ch in range(26):
                c += 1 if charcount[ch][r+1] - charcount[ch][l] > 0 else 0
            ans.append(True if c > 2 else False)
    
    print('\n'.join(['Yes' if v else 'No' for v in ans]))
    

s = input()
nq = int(input())
queries = []
for i in range(nq):
    l, r = map(int, input().split())
    queries.append((l-1, r-1))
solve(s, queries)
