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
created by shhuan at 2017/11/21 16:29

"""


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.nums = []
        self.numindex = collections.defaultdict(list)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        self.numindex[val].append(len(self.nums))
        self.nums.append((val, len(self.numindex[val]) - 1))

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.numindex:
            return False


        lastva, lastindex = self.nums[-1]
        self.numindex[lastva][lastindex] = self.numindex[val][-1]
        self.nums[self.numindex[val][-1]] = (lastva, lastindex)
        self.numindex[val].pop()
        if not self.numindex[val]:
            del self.numindex[val]

        self.nums.pop()

        return True




    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """

        i = random.randint(0, len(self.nums) - 1)

        return self.nums[i][0]





rd = RandomizedCollection()
rd.insert(4)
rd.insert(3)
rd.insert(4)
rd.insert(2)
rd.insert(4)
rd.remove(4)
rd.remove(4)
rd.remove(4)
rd.remove(4)
rd.getRandom()