# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/5 22:18

"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0

        N = len(clips)
        clips.sort()
        print(clips)
        r = max([v for u, v in clips if u == 0])
        ans = 1
        ri = 0
        while ri < N and r < T:
            nr = r
            while ri < N and clips[ri][0] <= r:
                nr = max(nr, clips[ri][1])
                ri += 1
            if r == nr:
                return -1
            r = nr
            ans += 1

        return ans if r >= T else -1

s = Solution()
print(s.videoStitching([[16,18],[16,20],[3,13],[1,18],[0,8],[5,6],[13,17],[3,17],[5,6]], 15))
# print(s.videoStitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10))
# print(s.videoStitching(clips = [[0,1],[1,2]], T = 5))
# print(s.videoStitching(clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9))
# print(s.videoStitching(clips = [[0,4],[2,8]], T = 5))
# print(s.videoStitching([[0, 2], [4, 8]], 5))