# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/22/18

"""



Q = int(input())

for qi in range(Q):
    N, M, K = map(int, input().split())
    
    if N < M:
        N, M = M, N
        
    if N % 2 != M % 2:
        K -= 1
        N -= 1
    elif N % 2 != K % 2:
        K -= 2
        N -= 1
        M -= 1
    
    print(-1 if K < N else K)