# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/21/18

"""
import collections

N = int(input())

G = collections.defaultdict(set)
for i in range(N-1):
    u, v = map(int, input().split())
    G[u].add(v)
    G[v].add(u)

A = [int(x) for x in input().split()]

if A[0] != 1:
    print("No")
    exit(0)

ai = 1
q = collections.deque([A[0]])
vis = [False] * (N+1)
vis[A[0]] = True
while q:
    u = q.popleft()
    
    vs = {v for v in G[u] if not vis[v]}
    if vs:
        if all([v in vs for v in A[ai: ai+len(vs)]]):
            for v in A[ai: ai+len(vs)]:
                vis[v] = True
                q.append(v)
            ai += len(vs)
        else:
            print("No")
            exit(0)
print("Yes")