# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/9/24 09:55

"""


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        data = [list('0' * (8 - len(v))) + v for v in [list(bin(v)[2:]) for v in data]]

        print(data)
        index = 0
        while index < len(data):
            d = data[index]
            if d[0] == '0':
                index += 1
                continue

            n = -1
            if d[:4].count('1') == 4 and d[4] == '0':
                n = 4
            elif d[:3].count('1') == 3 and d[3] == '0':
                n = 3
            elif d[:2].count('1') == 2 and d[2] == '0':
                n = 2
            if n > 0:
                if index + n <= len(data):
                    for i in range(index + 1, index + n):
                        if data[i][:2] != ['1', '0']:
                            return False
                else:
                    return False
                index += n

            else:
                return False

        return True

s = Solution()
print(s.validUtf8([145]))