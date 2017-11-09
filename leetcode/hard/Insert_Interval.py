# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/7 17:42

"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        def bisec(A, v, t):
            n = len(A)
            lo = 0
            hi = n
            while lo < hi:
                m = lo + (hi - lo) // 2
                u = A[m].start if t == 0 else A[m].end
                if u == v:
                    return m
                elif u < v:
                    lo = m + 1
                else:
                    hi = m
            return lo

        A = intervals
        N = len(A)
        b = newInterval
        c = bisec(A, b.start, 1)
        d = bisec(A, b.end, 0)

        if c < N and A[c].start < b.start:
            if d < N and A[d].start <= b.end:
                return A[:c] + [Interval(A[c].start, A[d].end)] + A[d + 1:]
            elif d < N:
                if d > 0 and A[d - 1].end > b.end:
                    return A[:c] + [Interval(A[c].start, A[d - 1].end)] + A[d:]
                else:
                    return A[:c] + [Interval(A[c].start, b.end)] + A[d:]
            else:
                return A[:c] + [Interval(A[c].start, max(b.end, A[-1].end))]
        elif c < N:
            if d < N and A[d].start <= b.end:
                return A[:c] + [Interval(min(A[c].start, b.start), A[d].end)] + A[d + 1:]
            else:
                if d > 0 and A[d - 1].end > b.end:
                    return A[:c] + [Interval(b.start, A[d - 1].end)] + A[d:]
                else:
                    return A[:c] + [Interval(b.start, b.end)] + A[d:]
        else:
            return A + [b]

s = Solution()
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[1, 5]]], Interval(0, 1))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[1,3],[6,9]]], Interval(2, 5))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[1,3],[6,9]]], Interval(2, 7))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[1,3],[6,9]]], Interval(2, 6))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[1,3],[6,9]]], Interval(3, 6))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[1,3],[6,9]]], Interval(3, 5))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[1,3],[6,9]]], Interval(4, 5))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[3,5],[6,9]]], Interval(1, 2))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[3,5],[6,9]]], Interval(1, 3))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[3,5],[6,9]]], Interval(1, 4))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[3,5],[6,9], [10, 12]]], Interval(1, 7))])
print([(v.start, v.end) for v in s.insert([Interval(v[0], v[1]) for v in [[3,5],[6,9], [10, 12]]], Interval(1, 11))])