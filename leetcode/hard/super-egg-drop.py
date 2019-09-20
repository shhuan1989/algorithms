# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/4 21:38


你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？



当前有N层，K个鸡蛋，设f(N,K)需要的次数，可以选择从第i层扔鸡蛋，有两种情况，碎或者不碎：
如果碎了，只能从第1到第i-1层里面尝试，总共需要 1 + f(i-1, K-1)次。
如果不碎，需要从第i+1到第N层里面尝试，总共需要 1 + (N-i, K)此。
很明显最少需要的次数需要覆盖这两种情况，即f(N, K, i) = 1 + max(f(i-1, K-1), f(N-i, K))。
而我们可以选择次数最小的那一层开始，所以f(N, K) = min{1 + max(f(i-1, K-1), f(N-i, K)) for i in [1, N]}


f(i-1, K-1)随着i增加而递增， f(N-i, K)随着i增加而递减，所以两个函数的交点即使最小值点。

观察到答案比较小，可以反过来找：
设f(T, K)表示T次操作，K个鸡蛋最多f(T, K)高的楼能够找到答案。
f(T, K) = 1 + f(T-1, K-1) + f(T-1, K)

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = range(N + 1)

        for k in range(2, K + 1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N + 1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x - 1], dp2[n - x]) > max(dp[x], dp2[n - x - 1]):
                    x += 1

                # The final answer happens at this x.
                dp2.append(1 + max(dp[x - 1], dp2[n - x]))

            dp = dp2

        return dp[-1]

        class Solution3(object):
            def superEggDrop(self, K, N):
                def f(x):
                    ans = 0
                    r = 1
                    for i in range(1, K + 1):
                        r *= x - i + 1
                        r //= i
                        ans += r
                        if ans >= N: break
                    return ans

                lo, hi = 1, N
                while lo < hi:
                    mi = (lo + hi) // 2
                    if f(mi) < N:
                        lo = mi + 1
                    else:
                        hi = mi
                return lo


    def superEggDrop_2(self, K: int, N: int) -> int:
        dp = [[float('inf') for _ in range(K+1)] for _ in range(N+1)]
        for i in range(N+1):
            dp[i][1] = i
        for k in range(K+1):
            dp[0][k] = 0

        for k in range(2, K+1):
            for n in range(1, N+1):
                dp[n][k] = 1 + min([max(dp[i-1][k-1], dp[n-i][k]) for i in range(1, n+1)])

        return dp[N][K]


s = Solution()
# print(s.superEggDrop(1, 2))
# print(s.superEggDrop(2, 6))
# print(s.superEggDrop(3, 14))
print(s.superEggDrop(2, 5000))