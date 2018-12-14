# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/11/18

"""

import collections
import sys

sys.stdin = open('input.txt', 'r')


def compare(duinda, duindb):
    da, inda = duinda
    db, indb = duindb
    if da != db:
        return da - db
    else:
        return indb - inda


def build_heap(du, idx, indegree):
    for i in range(len(du)):
        shift_up(du, i, idx, indegree)


def shift_up(du, i, idx, indegree):
    while i > 0:
        parent = (i - 1) // 2
        dt, ut = du[parent]
        di, ui = du[i]
        if compare((di, indegree[ui]), (dt, indegree[ut])) >= 0:
            idx[du[i][1]] = i
            break

        du[i], du[parent] = du[parent], du[i]
        idx[ui], idx[ut] = parent, i
        i = parent


def shift_down(du, idx, indegree):
    i = 0
    n = len(du)
    while i < n:
        l, r = i * 2 + 1, i * 2 + 2
        child = -1
        if l < n and compare((du[i][0], indegree[du[i][1]]), (du[l][0], indegree[du[l][1]])) > 0:
            child = l
        elif r < n and compare((du[i][0], indegree[du[i][1]]), (du[r][0], indegree[du[r][1]])) > 0:
            child = r
        else:
            idx[du[i][1]] = i
            break
        
        ui, ut = du[i][1], du[child][1]
        du[i], du[child] = du[child], du[i]
        idx[ui], idx[ut] = child, i
        i = child


def heap_pop(du, idx, indegree):
    ans = du[0]
    du[0] = du[-1]
    du.pop()
    if du:
        idx[du[0][1]] = 0
        shift_down(du, idx, indegree)

    return ans


def solve(N, M, E, G, D):
    if M % 2 != 0:
        print(-1)
        return []
    else:
        du = [[D[u], u] for u in range(1, N + 1)]
        idx = [0] * (N + 1)
        indegree = [0] * (N + 1)
        build_heap(du, idx, indegree)
        
        mark = set()
        while du:
            d, u = heap_pop(du, idx, indegree)
            print(u)
            if D[u] > 0:
                ind = indegree[u]
                vs = [v for v in G[u] if D[v] > 0]
                
                
                for vi, v in enumerate(vs):
                    direct = 1 if vi < ind % 2 == 1 else 0
                    D[u] -= 1
                    D[v] -= 1
                    iv = idx[v]
                    du[iv][0] -= 1
                    if direct == 1:
                        mark.add((v, u))
                        indegree[u] += 1
                        ind += 1
                    else:
                        mark.add((u, v))
                        indegree[v] += 1
                    shift_up(du, iv, idx, indegree)
        
        ans = []
        for u, v in E:
            if (u, v) in mark:
                ans.append(0)
            elif (v, u) in mark:
                ans.append(1)
            else:
                print(-1)
                return []
        print(' '.join(map(str, ans)))
        
        print(mark)
        
        return ans


def geninput():
    import random
    N= random.randint(6, 7)
    # N = 8
    E = set()
    for i in range(1, N):
        E.add((i, i+1))
    
    for i in range(random.randint(1, N*2)):
        u = random.randint(1, N)
        v = random.randint(u, N)
        if u != v:
            E.add((u, v))
    M = len(E)
    
    G = collections.defaultdict(list)
    E = list(E)
    D = [0] * (N + 1)
    for u, v in E:
        G[u].append(v)
        G[v].append(u)
        D[u] += 1
        D[v] += 1
    
    return N, M, E, G, D
    

def check(N, M, E, G, D, ans):
    if not ans:
        return True
    ind = collections.defaultdict(int)
    for i in range(M):
        u, v = E[i]
        if ans[i] == 0:
            ind[v] += 1
        else:
            ind[u] += 1
    
    return all([c % 2 == 0 for c in ind.values()])
    
    
    

# E = [(1, 2), (2, 6), (5, 6), (4, 5), (1, 4), (2, 3), (3, 6), (3, 4)]
# G = {1: [2, 4], 2: [1, 6, 3], 3: [2, 6, 4], 4: [5, 1, 3], 5: [6, 4], 6: [2, 5, 3]}
# D = [0, 2, 3, 3, 3, 2, 3]
# solve(6, 8, E, G, D)
# exit(0)
for ti in range(100000):
    N, M, E, G, D = geninput()
    try:
        ans = solve(N, M, E.copy(), G.copy(), D.copy())
        if not check(N, M, E, G, D, ans):
            raise Exception('error')
    except:
        print(N, M)
        print(E)
        print(G)
        print(D)
        print('======error=======')

        with open('input.txt', 'w') as f:
            f.write('1\n')
            f.write('{} {}\n'.format(N, M))
            for u, v in E:
                f.write('{} {}\n'.format(u, v))

        exit(0)


T = int(input())
for ti in range(T):
    N, M = map(int, input().split())
    G = collections.defaultdict(list)
    E = []
    D = [0] * (N+1)
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        E.append((u, v))
        D[u] += 1
        D[v] += 1

    ans = solve(N, M, E, G, D)
    print(check(N, M, E, G, D, ans))
    
    
