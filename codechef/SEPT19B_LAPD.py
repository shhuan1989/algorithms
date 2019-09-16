# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/11 21:30

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List

# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math

MOD = 10 ** 9 + 7
<<<<<<< HEAD

def mul(x, y):
    if y == 0:
        return 0
    if y == 1:
        return x

    if y % 2 == 0:
        return (mul(x, y//2)*2) % MOD

    return (mul(x, y // 2) * 2 + x) % MOD

# X = [0 for _ in range(5000)]
=======
# t0 = time.time()

MAXN = 5005
# X = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
Y = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
for b in range(1, MAXN):
    b2 = b**2
    for c in range(1, min(b2+2, MAXN)):
        # X[b][c] = b // c
        
        Y[b][c] = b2//c + Y[b][c - 1]
        

# print('init time: {}'.format(time.time() - t0))
>>>>>>> add codechef

# b**2 < (a-1)*(c-1)
def solve(A, B, C):
    if A == 1 or C == 1:
        return 0
<<<<<<< HEAD

    ans = 0
    pc, pa = 0, 0
    pp, pb, pb2 = 0, 0, 0
    for b in range(1, B + 1):
        b2 = b ** 2
        a = max(A - (b + 1), 0)
        c = max(C - (b + 1), 0)
        if a > 0 and c > 0:
            pp += 1
            pb += b+1
            pb2 += (b+1)**2


        # ans += a*c
        # ans %= MOD

        al, ar = max(b2//(C-1)+1, 1), min(A, b + 1)
        if ar > al:
            pc += ar-al
            ans += MOD - sum([b2 // a for a in range(al, min(ar, b2//2+1))]) - max(0, ar-b2//2-1)
            ans %= MOD

        cl, cr = max(b2//(A-1)+1, 1), min(C, b + 1)
        if cr > cl:
            pa += cr-cl
            ans += MOD - sum([b2 // c for c in range(cl, min(cr, b2//2+1))]) - max(0, cr-b2//2-1)
            ans %= MOD

    ans += pc*(C-1)
    ans %= MOD
    ans += pa*(A-1)
    ans %= MOD
    ans += A*C*pp
    ans %= MOD
    ans += pb2
    ans %= MOD
    ans = ans + MOD - pb*(A+C)
    ans %= MOD

    print(pc, pa, B)
    return ans



import random
t0 = time.time()
for i in range(10):
    A, B, C = random.randint(10**8, 10**9), random.randint(4000, 5000), random.randint(10**8, 10**9)
    # A, B, C = random.randint(4000, 5000), random.randint(4000, 5000), random.randint(4000, 5000)


    print(solve(A, B, C))
print(time.time() - t0)
=======
    
    A -= 1
    C -= 1
    ans = 0
    # lens = []
    for b in range(1, B + 1):
        b2 = b ** 2
        a = max(A - b, 0)
        c = max(C - b, 0)
        ans += a * c
        ans %= MOD

        # xy = [(x, b2//x) ]
        # ans += sum([(max(C-b2//x, 0) if x <= A else 0) + (max(A-b2//x, 0) if x <= C else 0) for x in range(min(b, max(A, C)), max(b2 // (max(A, C) - 1) - 1, 0), -1)])
        # ans %= MOD
        
        # b2//x+1 > max(A, C) = >
        # for x in range(min(b, max(A, C)), max(b2//(max(A, C)-1)-1, 0), -1):
        #     y = b2 // x + 1
        #     # if y > max(A, C):
        #     #     break
        #     if x <= A:
        #         ans += max(C-y+1, 0)
        #     if x <= C:
        #         ans += max(A-y+1, 0)
        #     ans %= MOD
        
        al, ar = max(b2//C+1, 1), min(A, b) + 1
        if al < ar:
            # lens.append(ar-al)
            ans += C * (ar - al) - (Y[b][ar-1]-Y[b][al-1])
            # ans += C*(ar-al) - sum(b2//a for a in range(al, ar))
            ans %= MOD

        cl, cr = max(b2//A+1, 1), min(C, b) + 1
        if cl < cr:
            # lens.append(cr-cl)
            ans += A*(cr-cl) - (Y[b][cr-1] - Y[b][cl-1])
            # ans += A*(cr-cl) - sum(b2//c for c in range(cl, cr))
            ans %= MOD
    # print('lens', sum(lens))
    return ans


# import random
# t0 = time.time()
# for i in range(10):
#     A, B, C = random.randint(10**8, 10**9), random.randint(4000, 5000), random.randint(10**8, 10**9)
#     print(solve(A, B, C))
# print(time.time() - t0)
>>>>>>> add codechef


T = int(input())
for ti in range(T):
    A, B, C = map(int, input().split())
    print(solve(A, B, C))