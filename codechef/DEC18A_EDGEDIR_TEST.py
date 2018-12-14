# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/12/18

"""
import collections
import subprocess

def geninput():
    import random
    N = random.randint(3, 6)
    E = set()
    for i in range(1, N):
        E.add((i, i + 1))
    
    for i in range(random.randint(1, N * 2)):
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


for i in range(10000000):
    N, M, E, G, D = geninput()
    with open('input.txt', 'w') as f:
        input = ['1\n']
        input.append('{} {}\n'.format(N, M))
        for u, v in E:
            input.append('{} {}\n'.format(u, v))
        f.writelines(input)
        f.close()

    ans = []
    for code in ['DEC18A_EDGEDIR.py', 'DEC18A_EDGEDIR2.py']:
        p = subprocess.Popen(['/anaconda2/envs/tf35/bin/python', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='./')
        stdout, stderr = p.communicate()
        ans.append(stdout.decode('utf-8'))
    
    if ans[0] != ans[1]:
        print(N, M)
        print(E)
        print(G)
        print(D)
        print(ans[0])
        print(ans[1])
        exit(0)
    
