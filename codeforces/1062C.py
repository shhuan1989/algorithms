# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/19/18

"""

N, M = map(int, input().split())
A = input()
#
# import random
# import time
# N, M = 10**5, 10**5
# A = ''.join(['1' if random.randint(1, 10) < 6 else '0' for _ in range(N)])
# print('starting...')
# t0 = time.time()

MOD = 10**9+7

left = [0] * (N+1)
for i in range(1, N+1):
    left[i] = left[i-1] + int(A[i-1])

ans = []
for qi in range(M):
    l, r = map(int, input().split())
    # l = random.randint(1, N)
    # r = random.randint(l, N)
    ones = left[r] - left[l-1]
    zeros = r-l+1-ones
    x = (1 << ones) - 1
    x %= MOD
    y = (1 << zeros)-1
    y %= MOD
    ans.append((x+x*y) % MOD)
    
    
print('\n'.join(map(str, ans)))

# print(time.time() - t0)
