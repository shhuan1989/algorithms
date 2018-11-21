# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/21/18

"""

N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
B = [int(x) for x in input().split()]

ans = 0

i, j = 0, 0
sa, sb = 0, 0
while i < N or j < M:
    if sa == sb:
        ans += 1
        if i < N:
            sa += A[i]
            i += 1
        if j < M:
            sb += B[j]
            j += 1
    elif sa < sb:
        if i < N:
            sa += A[i]
            i += 1
        else:
            break
    else:
        if j< M:
            sb += B[j]
            j += 1
        else:
            break

if i == N and j == M and sa == sb:
    print(ans)
else:
    print(-1)