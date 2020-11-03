# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/28

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    start = input().strip()
    target = '123804765'
    
    def tomatrix(s):
        return [list(s[:3]), list(s[3: 6]), list(s[6:])]
    
    def tostate(m):
        return ''.join([''.join(row) for row in m])
    
    def move(s):
        m = tomatrix(s)
        i = s.index('0')
        x = i // 3
        y = i % 3
        
        ns = []
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < 3 and 0 <= ny < 3:
                m[nx][ny], m[x][y] = m[x][y], m[nx][ny]
                ns.append(tostate(m))
                m[nx][ny], m[x][y] = m[x][y], m[nx][ny]
        
        return ns
    
    q = [start]
    vis = {start}
    step = 0
    while q:
        # print(q)
        nq = []
        for s in q:
            if s == target:
                print(step)
                exit(0)
            for ns in move(s):
                if ns not in vis:
                    nq.append(ns)
                    vis.add(ns)
        q = nq
        step += 1
    
    
    