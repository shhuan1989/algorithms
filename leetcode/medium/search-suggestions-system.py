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
created by shhuan at 2019/11/24 10:42

"""

from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        for i, w in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == w]
            products.sort()
            ans.append(products[:3])

        return ans


s = Solution()
print(s.suggestedProducts( ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))
print(s.suggestedProducts(products = ["havana"], searchWord = "havana"))
print(s.suggestedProducts(products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"))
print(s.suggestedProducts(products = ["havana"], searchWord = "tatiana"))