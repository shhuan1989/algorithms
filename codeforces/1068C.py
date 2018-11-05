# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/3/18



                         6
                 5       |
            4    |       |
       3    |    |       |
    2  |    |    |       |
1   |  |    |    |       |
1---2  |    |    |       |
    2--3    |    |       |
    2-------4    |       |
                 5-------6
"""


N, M = map(int, input().split())


ans = [(0, 0)] + [[(i+1, i+10000)] for i in range(N)]

y = 9999
for mi in range(M):
    u, v = map(int, input().split())
    ans[u].append((u, y))
    ans[v].append((v, y))
    y -= 1
    

outs = []
for i in range(1, N+1):
    outs.append(str(len(ans[i])))
    for x, y in ans[i]:
        outs.append('{} {}'.format(x, y))
print('\n'.join(outs))
