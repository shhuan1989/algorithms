# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/11/18

"""

import collections
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for ti in range(T):
    N, M = map(int, input().split())
    G = collections.defaultdict(list)
    E = []
    D = collections.defaultdict(int)
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        E.append((u, v))
        D[u] += 1
        D[v] += 1
    
    if M % 2 != 0:
        print(-1)
    else:
        mark = {}
        indegree = collections.defaultdict(int)
        while D:
            dmin = min(D.values())
            us = [u for u, d in D.items() if d == dmin]
            usin = [(indegree[u], u) for u in us]
            usin.sort()
            ind, u = usin[0]
            
            print(u)
            # d = ind + dmin
            for v in G[u]:
                if (u, v) not in mark and (v, u) not in mark:
                    direct = 0 if ind % 2 == 0 else 1
                    mark[(u, v)] = direct
                    ind += direct
                    D[v] -= 1
                    D[u] -= 1
                    if direct == 0:
                        indegree[v] += 1
                    else:
                        indegree[u] += 1
            
            D = {u: d for u, d in D.items() if d > 0}
        
        ans = []
        for u, v in E:
            if (u, v) in mark:
                ans.append(mark[(u, v)])
            elif (v, u) in mark:
                ans.append(mark[(v, u)] ^ 1)
            else:
                print(-1)
                exit(0)
        print(' '.join(map(str, ans)))

        mks = []
        for i in range(len(ans)):
            if ans[i] == 0:
                mks.append((E[i]))
            else:
                mks.append((E[i][1], E[i][0]))
        print(mks)
        
        wc = collections.defaultdict(int)
        for u, v in mks:
            wc[v] += 1
        if any([x % 2 != 0 for x in wc.values()]):
            print('error')
        else:
            print('correct')