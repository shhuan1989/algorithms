# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/17/18

"""

import collections
import heapq


N, M, K = map(int, input().split())

G = collections.defaultdict(list)
for i in range(M):
    x, y, w = map(int, input().split())
    G[x].append((y, w, i+1))
    G[y].append((x, w, i+1))

dists = [float('inf') for _ in range(N+1)]
dists[1] = 0
q = [(0, 1, 0)]
heapq.heapify(q)
visited = [False for _ in range(N+1)]
ans = []
while q:
    if len(ans) > K:
        break
    wu, u, idx = heapq.heappop(q)

    if not visited[u]:
        visited[u] = True
        ans.append(idx)
    
        for v, w, vidx in G[u]:
            d = wu + w
            if not visited[v] and d < dists[v]:
                dists[v] = d
                heapq.heappush(q, (d, v, vidx))

# SPFA
# q = [1]
# visited = {1}
# while q:
#     u = q.pop()
#     visited.discard(u)
#     for v, w, idx in G[u]:
#         d = dists[u] + w
#         if v not in visited and d < dists[v]:
#             dists[v] = d
#             q.append(v)
# print(dists)

print(len(ans) - 1)
print(" ".join(map(str, ans[1:])))