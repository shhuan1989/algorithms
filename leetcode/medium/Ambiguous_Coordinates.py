# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/22 14:48

"""


class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """


        def norm(val):
            di = val.find('.')

            while val[0] == '0' and len(val) > 1 and val[1] != '.':
                val = val[1:]

            i = 0
            while i < len(val) and val[i] != '.':
                i += 1

            if i < len(val):
                while val[-1] == '0':
                    val = val[:-1]
            if val[-1] == '.':
                val = val[:-1]

            return val

        def nums(val):
            if not val:
                return []
            ans = [val] + ['{}.{}'.format(val[:i], val[i:]) for i in range(1, len(val))]
            ans = [x for x in ans if norm(x) == x]

            return ans

        S = S[1: -1]

        ans = []
        for i in range(1, len(S)):
            a, b = S[:i], S[i:]
            for x in nums(a):
                for y in nums(b):
                    ans.append('({}, {})'.format(x, y))

        return ans

s = Solution()
print(s.ambiguousCoordinates("(00011)"))
print(s.ambiguousCoordinates("(100)"))
print(s.ambiguousCoordinates("(0010)"))