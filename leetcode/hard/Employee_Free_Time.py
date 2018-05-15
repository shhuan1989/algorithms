# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
import functools

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """

        if not schedule:
              return []

        scs = [self.freeTimes(s) for s in schedule]
        ans = functools.reduce(lambda x, y: self.merge(x, y), scs)
        ans = filter(lambda x: x[0] > float('-inf') and x[1] < float('inf'), ans)

        # return list(ans)
        return [Interval(x[0], x[1]) for x in ans]


    def merge(self, s1, s2):
          if not s1 or not s2:
          return []

      ans = []
      for a in s1:
        for b in s2:
          if a == b:
            ans.append(a)
          else:
            if b[0] <= a[1] <= b[1]:
              ans.append((max(a[0], b[0]), a[1]))
            elif a[0] <= b[1] <= a[1]:
              ans.append((max(a[0], b[0]), b[1]))

      return list(filter(lambda x: x[1] > x[0], ans))


    def freeTimes(self, schedule):
      if not schedule:
        return []
      ans = [(float('-inf'), schedule[0].start)]
      # ans = [(float('-inf'), schedule[0][0])]
      for i in range(len(schedule)-1):
        ans.append((schedule[i].end, schedule[i+1].start))
        # ans.append((schedule[i][1], schedule[i + 1][0]))

      ans.append((schedule[-1].end, float('inf')))
      # ans.append((schedule[-1][1], float('inf')))

      return ans


s = Solution()


print(s.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]))
print(s.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))
