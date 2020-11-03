# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)
        player = [(ages[i], scores[i]) for i in range(n)]
        player.sort()
        
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = player[i][1]
            for j in range(i):
                if player[j][1] <= player[i][1]:
                    dp[i] = max(dp[i], dp[j] + player[i][1])
        
        # print(player)
        # print(dp)
        return max(dp)
        
        
if __name__ == '__main__':
    s = Solution()
    # print(s.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
    print(s.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
    # print(s.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))
    # print(s.bestTeamScore([1,1,1,1,1,1,1,1,1,1], [811,364,124,873,790,656,581,446,885,134]))
    # print(s.bestTeamScore([648,374,437,279,258,223,225,802,744,537,60,524,991,20,462,359,208,577,515,734,233,217,548,947,511,653,237,315,824,480,741], [16,55,21,48,23,7,27,37,99,33,26,76,84,1,45,78,84,89,64,99,97,28,23,91,32,97,68,84,57,7,65]))
    # print(s.bestTeamScore([674,918,473,933,161,82,874,131,367,941,799,488,222,778,352,411,585,833,310,988,807,230,251,187,222,125,112,273,978,109,14,485,955,761,922,658,144,42,124,893,181,911,567,587,28,562,666,871,275,587,437,826,502,354,704,979,868,520,661,163,805,250],[59,30,1,28,36,95,30,5,61,23,78,6,47,14,26,47,88,98,23,92,9,77,30,39,4,59,51,64,73,1,58,23,63,70,44,51,62,92,70,92,66,5,80,36,9,95,100,3,11,90,71,57,78,45,4,66,90,45,26,79,1,80]))