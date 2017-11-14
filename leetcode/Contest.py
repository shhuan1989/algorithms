# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/8 09:18
    
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """



        def dfs(fm):

            i = 0
            count = collections.defaultdict(int)
            while i < len(fm) and fm[i] != '(' and fm != ')':
                if fm[i].isupper():
                    j = i + 1
                    while j < len(fm) and fm[j].islower():
                        j += 1
                    e = fm[i:j]
                    k = j
                    while k < len(fm) and fm[k].isnumeric():
                        k += 1
                    if k > j:
                        count[e] = int(fm[j: k])
                    else:
                        count[e] = 1
                    i = k
                else:
                    i += 1


