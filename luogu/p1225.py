# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/28

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    start = 0
    target = 0
    for i in range(4):
        start *= 16
        start += int(input().strip(), 2)
    
    for i in range(4):
        target *= 16
        target += int(input().strip(), 2)
        
    def swap(s, r1, c1, r2, c2):
        r1 = 4 - r1 - 1
        c1 = 4 - c1 - 1
        r2 = 4 - r2 - 1
        c2 = 4 - c2 - 1
        a = r1 * 4 + c1
        b = r2 * 4 + c2
        
        if s & (1 << a) == s & (1 << b):
            return s
        
        s ^= 1 << a
        s ^= 1 << b
        return s
        
    def neibs(r, c):
        return [(nr, nc) for nr, nc in [(r+1, c), (r, c+1)] if 0 <= nr < 4 and 0 <= nc < 4]
    
    vis = {start}
    pre = {}
    op = {}
    q = [start]
    while q:
        nq = []
        for s in q:
            if s == target:
                ans = []
                st = s
                while st in pre:
                    ans.append(op[st])
                    st = pre[st]
                print(len(ans))
                print('\n'.join(reversed(ans)))
                exit(0)
            
            for r in range(4):
                for c in range(4):
                    for nr, nc in neibs(r, c):
                        t = swap(s, r, c, nr, nc)
                        if t not in vis:
                            nq.append(t)
                            vis.add(t)
                            pre[t] = s
                            op[t] = '{}{}{}{}'.format(r+1, c+1, nr+1, nc+1)
                        swap(s, r, c, nr, nc)
        q = nq
