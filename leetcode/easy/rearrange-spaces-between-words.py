# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/20 10:30

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


class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        blank = text.count(' ')
        words = [w for w in text.split(' ') if len(w) > 0]
        if len(words) == 1:
            return words[0] + ' ' * blank

        gap = blank // (len(words) - 1)

        ans = ' ' * gap
        ans = ans.join(words)
        ans += ' ' * ( blank % (len(words)-1))

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.reorderSpaces('  this   is  a sentence ') == 'this   is   a   sentence')
    print(s.reorderSpaces(' practice   makes   perfect') == "practice   makes   perfect ")
    print(s.reorderSpaces('hello   world') == "hello   world")
    print(s.reorderSpaces("  walks  udp package   into  bar a") == "walks  udp  package  into  bar  a ")
    print(s.reorderSpaces('a') == 'a')