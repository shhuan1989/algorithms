# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import cmp_to_key

if __name__ == '__main__':
    # sys.stdin = open('P1347_2.in', 'r')
    N, M = map(int, input().split())
    
    g = [[] for _ in range(N)]
    ind = [0 for _ in range(N)]
    nodes = set()
    def check():
        indc = ind.copy()
        
        q = [u for u in nodes if indc[u] == 0]
        if not q:
            return True, False
            
        dist = [0 for _ in range(N)]
        q = collections.deque(q)
        for u in q:
            dist[u] = 1
        while q:
            u = q.popleft()
            if dist[u] > N:
                return True, False
            for v in g[u]:
                if dist[v] < dist[u] + 1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        if len(nodes) == N and max(dist) == N:
            ans = [i for i in range(N)]
            ans.sort(key=cmp_to_key(lambda u, v: dist[u]-dist[v]))
            ans = ''.join([chr(ord('A')+v) for v in ans])
            return False, ans
        
        if len([u for u in range(N) if dist[u] > 0]) != len(nodes):
            return True, False
        return False, False
        
    for step in range(M):
        u, v = input().strip().split('<')
        u = ord(u) - ord('A')
        v = ord(v) - ord('A')
        nodes.add(u)
        nodes.add(v)
        
        g[u].append(v)
        ind[v] += 1
        cycle, ans = check()
        if cycle:
            print('Inconsistency found after {} relations.'.format(step+1))
            exit(0)
        if ans:
            print('Sorted sequence determined after {} relations: {}.'.format(step+1, ans))
            exit(0)
        
    print('Sorted sequence cannot be determined.')