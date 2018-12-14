# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/13/18

"""

import collections

N = int(input())
D = collections.defaultdict(int)
MOD = 10**9+7
G = collections.defaultdict(list)
for i in range(N-1):
    u, v = map(int, input().split())
    D[u] += 1
    D[v] += 1
    G[u].append(v)
    G[v].append(u)


ans = [0] * (N+1)

nodes = {}
for i in range(1, N+1):
    nodes[(i)] = i

def pow2(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    
    h = pow2(x //2)
    ans = h * h if x % 2 == 0 else h * h * 2
    
    return ans % MOD

nodecounts = collections.defaultdict(int)
for i in range(1, N+1):
    nodecounts[i] = 1

number = N
states = {i for i in range(1, N+1)}
n = (N-1)*(N-2)//2
ans[N] = 1

while True:
    nstates = set()
    components = len(states)
    if components < 3:
        break
        
    us = [u for u, d in D.items() if u in states and d == 1]
    vis = set()
    for u in us:
        if u in vis:
            continue
        vis.add(u)
        v = G[u][0]
        for w in G[v]:
            if w in vis:
                continue
            vis.add(w)
            # connect u, v
            x = tuple(list(sorted([u, v, w])))
            if x in nodes:
                x = nodes[x]
                # continue
            else:
                number += 1
                nodes[x] = number
                x = number
            nodecounts[x] = nodecounts[u] +nodecounts[w] + nodecounts[v]
            D[x] = D[v]-2
            s = tuple(sorted((states - {u, v, w}) | {x}))
            # if s in nstates:
            #     continue
            
            nstates.add(s)
            
            e = nodecounts[u] * nodecounts[w]
    
            # ans[components-2] += (1-1/(2**e))
            z = components * (components - 3) // 2
            ans[components - 2] += (pow2(n-z) + MOD - pow2(n-z-e)) % MOD
            ans[components - 2] %= MOD
    
    states = nstates
    
print(' '.join(map(str, ans[1: ])))