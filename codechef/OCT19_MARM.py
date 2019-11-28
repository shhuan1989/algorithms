# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/9/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


def baseline(A, N, K):
    for i in range(K):
        A[i%N] ^= A[N-(i%N)-1]
    
    return A

def solve(A, N, K):
    if N == 1:
        return [0]
    
    if N % 2 != 0 and K > N // 2:
        A[N//2] = 0
        
    if N % 2 == 0:
        l = N // 2 * 3
        m = K // l
        K %= l
        
        if m % 2 != 0:
            for i in range(N // 2):
                A[i], A[N-i-1] = A[N-i-1], A[i]
        if m % 2 != 0:
            for i in range(N//2, N//2+K):
                A[i%N] ^= A[(2*N - i - 1) % N]
        else:
            for i in range(K):
                A[i % N] ^= A[(2 * N - i - 1) % N]
    else:
        l = 3 * N
        K %= l
        for i in range(K):
            A[i % N] ^= A[(2 * N - i - 1) % N]
            
    return A


# def test():
#     import random
#
#     for i in range(10000):
#         N, K = random.randint(1, 10), random.randint(1, 10)
#         # N, K = 3, 6
#         A = [random.randint(1, 10) for _ in range(N)]
#         a, b = baseline(A.copy(), N, K), solve(A.copy(), N, K)
#         if a != b and N % 2 != 0:
#             solve(A.copy(), N, K)
#             print(a, b)
#         else:
#             # print(a, b)
#             pass
#         if i % 1000 == 0:
#             print(i)
#     print('test done!')
# solve([2, 2, 7], 3, 6)
# test()

T = int(input())
for ti in range(T):
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    print(' '.join(map(str, solve(A, N, K))))
        