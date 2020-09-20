# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/17 09:24

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

        q = []

        ans = 0
        for v in s:
            if v == ')':
                if q and q[-1] == ')':
                    q.pop()
                    if not q:
                        ans += 1
                    elif q[-1] == '(':
                        q.pop()
                else:
                    q.append(v)
            else:
                if q and q[-1] == ')':
                    q.pop()
                    if q:
                        if q[-1] == ')':
                            q.pop()
                            if q and q[-1] == '(':
                                q.pop()
                            else:
                                ans += 1
                        else:
                            q.pop()
                            ans += 1
                    else:
                        ans += 2
                q.append(v)

        while q:
            if q[-1] == '(':
                ans += 2
                q.pop()
            elif q[-1] == ')':
                q.pop()
                if q:
                    if q[-1] == ')':
                        q.pop()
                        if q and q[-1] == '(':
                            q.pop()
                        else:
                            ans += 1
                    else:
                        q.pop()
                        ans += 1

                else:
                    ans += 2

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minInsertions('(()))'))
    print(s.minInsertions('())'))
    print(s.minInsertions('))())('))
    print(s.minInsertions('(((((('))
    print(s.minInsertions(')))))))'))
    print(s.minInsertions('(()))(()))()())))'))