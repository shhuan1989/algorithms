# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/13/18

"""

import collections
import heapq

N, M = map(int, input().split())

G = collections.defaultdict(list)
outdegree = [0] * (N+1)
indegree = [0] * (N+1)
for i in range(M):
    u, v = map(int, input().split())
    G[v].append(u)
    outdegree[u] += 1
    indegree[v] += 1
    

q = [(-indegree[u], u) for u in range(1, N+1) if outdegree[u] == 0]
heapq.heapify(q)
ans = []

while q:
    removed = [heapq.heappop(q)[1]]
    if q:
        removed.append(heapq.heappop(q)[1])
    
    for u in removed:
        for v in G[u]:
            outdegree[v] -= 1
            if outdegree[v] == 0:
                heapq.heappush(q, (-indegree[v], v))
    
    ans.append(removed)

print(len(ans))
ans = ['{} {}'.format(len(x), ' '.join(map(str, x))) for x in ans]
print('\n'.join(ans))