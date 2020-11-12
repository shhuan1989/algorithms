# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/12

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List



if __name__ == '__main__':
    
    price = 170
    
    amount = [0]
    cost = [0]
    prices = [price]
    gap = 0.2
    while price > 50:
        amount.append(amount[-1] + 100)
        cost.append(cost[-1] + 100 * price)
        price *= 1 - gap
        prices.append(price)
    
    print('avg price {}'.format(cost[-1] / amount[-1]))
    print('total cost {}'.format(cost[-1]))
    print('hold {}'.format(amount[-1]))
    print(prices)
    print(cost)
    print(amount)