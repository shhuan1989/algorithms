# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/20/18

F[i][x][0] = 0
F[i][x][1] = 2
F[i+1][0][k] = F[i][0][k] + F[i][1][k] + F[i][2][k] + F[i][3][k-1]

out of memory, same code pass in c++

"""


# N, K = map(int, input().split())
N, K = 1000, 1000

import time
t0 = time.time()

dp = [[[0 for _ in range(max(K+1, 3))] for _ in range(4)] for _ in range(N+1)]

for i in range(N):
    dp[i][0][1] = 1
    dp[i][3][1] = 1

MOD = 998244353

dp[0][1][2] = 1
dp[0][2][2] = 1

for i in range(N-1):
    for k in range(2, min(K+1, 2*(i+2)+1)):
        dp[i+1][0][k] = (dp[i][0][k] + dp[i][1][k] + dp[i][2][k] + dp[i][3][k-1]) % MOD
        dp[i+1][1][k] = (dp[i][0][k-1] + dp[i][1][k] + dp[i][2][k-2] + dp[i][3][k-1]) % MOD
        dp[i + 1][2][k] = (dp[i][0][k-1] + dp[i][1][k-2] + dp[i][2][k] + dp[i][3][k - 1]) % MOD
        dp[i + 1][3][k] = (dp[i][0][k-1] + dp[i][1][k] + dp[i][2][k] + dp[i][3][k]) % MOD

ans = sum([dp[N-1][j][K] for j in range(4)])

print(ans % MOD)

print(time.time() - t0)