# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/29/18

"""


N, M = map(int, input().split())

A, D = [(0, 0)], []

for i in range(1, N+1):
    x, y = map(int, input().split())
    A.append((x, y))
    D.append((x-y, x, y, i))


D.sort()
D = [(0, 0, 0, 0)] + D

ans = [0] * (N+1)

rightY = [0] * (N+2)
leftX = [0] * (N+2)

for i in range(N, 0, -1):
    rightY[i] = rightY[i+1] + D[i][2]

for i in range(1, N+1):
    leftX[i] = leftX[i-1] + D[i][1]
    

for id in range(1, N+1):
    _, x, y, i = D[id]
    ans[i] += leftX[id-1] + (id-1) * y
    ans[i] += rightY[id+1] + (N-id) * x
    

for i in range(M):
    u, v = map(int, input().split())
    score = min(A[u][0] + A[v][1], A[u][1] + A[v][0])
    ans[u] -= score
    ans[v] -= score
    
    
print(' '.join(map(str, ans[1:])))