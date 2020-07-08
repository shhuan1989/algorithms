# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def subsidy(val, price_sale, expect):
    base = price_sale[0][0]
    profit = [(p-base+val)*s for p, s in price_sale]
    
    maxp = float('-inf')
    expectp = float('-inf')
    for i, p in enumerate(profit):
        if p > maxp:
            maxp = p
        if price_sale[i][0] == expect:
            expectp = p
            
        
    return maxp <= expectp


def solve(price_sale, expect):
    # print(price_sale)
    # print(expect)
    for p in range(1000000):
        if subsidy(p, price_sale, expect):
            return p
        if subsidy(-p, price_sale, expect):
            return -p
        
    return 'NO SOLUTION'


if __name__ == '__main__':
    expect = int(input())
    price_sale = []
    while True:
        p, s = map(int, input().split())
        if p == -1 and s == -1:
            break
        price_sale.append((p, s))
    delta = int(input())
    
    aps = []
    for p, s in price_sale:
        if aps and aps[-1][0] < p - 1:
            lastp, lasts = aps[-1]
            d = (lasts-s)//(p-lastp)
            for mp in range(lastp+1, p):
                aps.append((mp, lasts-(mp-lastp)*d))
        aps.append((p, s))
    
    aps += [(aps[-1][0]+i, aps[-1][1]-i*delta) for i in range(1, aps[-1][1]//delta+1)]
    price_sale = aps
    # print(price_sale)
    print(solve(price_sale, expect))