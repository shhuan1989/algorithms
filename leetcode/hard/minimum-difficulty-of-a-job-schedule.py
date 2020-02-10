# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/26/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        dp = [[float('inf') for _ in range(N+1)] for _ in range(d+1)]
        dp[0][0] = 0
        
        
        maxval = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            maxval[i][i] = jobDifficulty[i]
            for j in range(i+1, N):
                maxval[i][j] = max(maxval[i][j-1], jobDifficulty[j])
        
        
        for i in range(1, d+1):
            for j in range(i, N+1):
                for k in range(j):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + maxval[k][j-1])
        
        # for row in dp:
        #     print(row)
        return dp[d][N] if dp[d][N] < float('inf') else -1

    
s = Solution()
print(s.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))
print(s.minDifficulty(jobDifficulty = [9,9,9], d = 4))
print(s.minDifficulty(jobDifficulty = [1,1,1], d = 3))
print(s.minDifficulty(jobDifficulty = [7,1,7,1,7,1], d = 3))
print(s.minDifficulty(jobDifficulty = [11,111,22,222,33,333,44,444], d = 6))
print(s.minDifficulty([641,915,240,922,191,820,413,871,515,360,78,547,790,335,846,132,344,62,582,159,662,14,614,364,802,981,679,956,831,142,707,391,81,842,365,743,825,849,767,798,841,194,287,720,948,706,559,688,41,63,624,854,788,180,171,316,302,595,684,984,666,914,0,611,451,648,966,100,135,787,942,773,273,426,187,65,161,163,324,207,911,58,334,849,727,380,354,574,223,653,602,879,183,273,904,669,214,434,220,112,176,196,471,736,377,946,279,308,590,646,977,548,995,119,440,365,893,522,604,79,399,484,240,165,64,505,446,257,17,148,825,239,45,491,801,378,513,311,616,263,511,787,944,395,453,949,327,521,701,529,535,988,525,872,299,594,881,258,304,410,162,70,770,630,573,248,226,101,333,814,540,135,609,754,177,656,262,981,80,941,266,742,818,167,764,191,662,179,321,942,389,173,801,637,463,483,984,335,283,400,498,526,59,32,945,914,924,34,637,225,866,61,499,777,110,425,8,777,189,446,505,993,657,992,216,496,522,816,524,587,97,210,807,55,286,556,812,79,161,618,616,990,400,605,91,146,520,59,724,311,935,134,606,737,40,944,101,893,50,438,635,774,360,748,745,571,7,200,288,642,698,411,977,261,839,228,472,938,483,699,682,931,480,710,618,158,775,801,434,816,599,893,314,190,104,720,416,196,515,864], 4))