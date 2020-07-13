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
created by shhuan at 2020/7/12 12:23

"""


class Solution:
    def reformatDate(self, date: str) -> str:
        MONTH = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        dmy = date.strip().split( )
        year = dmy[-1]
        month = str(MONTH.index(dmy[1]) + 1)
        if len(month) < 2:
            month = '0' + month
        day = '0'
        for i in range(len(dmy[0])):
            if dmy[0][i].isalpha():
                day = dmy[0][:i]
                break
        if len(day) < 2:
            day = '0' + day

        return '{}-{}-{}'.format(year, month, day)