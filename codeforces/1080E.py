# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/27/18

"""

import collections

# N, M = map(int, input().split())
# A = []
# for i in range(N):
#     A.append(list(input()))

N, M = 250, 250
A = []
for i in range(N):
    A.append('a'*M)
    
ans = 0

left = [[0 for _ in range(M+1)] for _ in range(N)]
right = [[0 for _ in range(M+1)] for _ in range(N)]
for r in range(N):
    h = 0
    for c in range(M):
        h += ord(A[r][c])
        left[r][c+1] = h
    h = 0
    for r in range(M-1, -1, -1):
        h += ord(A[r][c])
        right[r][c] = h
        
for r in range(N):
    for c in range(M):
        for l in range(1, M-c+1):
            if l % 2 == 0:
                if left[c+l//2+1]-left[c] == right[c+l//2]-right[c+l]:
                    pass


#
#
# for r in range(N):
#     for c in range(M):
#         for l in range(1, M-c+1):
#             wc = B[r][c+l] - B[r][c]
#             if sum([1 if x % 2 == 1 else 0 for x in wc.values()]) <= 1:
#                 ans += 1
#                 for h in range(r+1, N):
#                     a = r
#                     b = h
#                     p = True
#                     while a < b:
#                         if B[a][c + l] - B[a][c] != B[b][c+l] - B[b][c]:
#                             p = False
#                             break
#                         a += 1
#                         b -= 1
#                     if p:
#                         ans += 1

print(ans)