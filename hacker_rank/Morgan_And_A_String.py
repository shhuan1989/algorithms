# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-07-11

"""

import collections
import time
import os
import sys
import bisect
import heapq


def suffixArray(anStr):
    if not anStr:
        return []
    
    chs = list(sorted(set(anStr)))
    ranks = {c: i for i, c in enumerate(chs)}
    
    # rank, prank, index
    n = len(anStr)
    suffix = [[ranks[v], ranks[anStr[i + 1]] if i < n - 1 else -1, i] for i, v in enumerate(anStr)]
    suffix.sort()
    
    k = 4
    ind = [0] * n
    while k < 2 * n:
        rank, prank = suffix[0][0], suffix[0][0]
        for i in range(1, n):
            if suffix[i][0] != prank or suffix[i][1] != suffix[i - 1][1]:
                rank += 1
            prank = suffix[i][0]
            suffix[i][0] = rank
            ind[suffix[i][2]] = i
        
        for i in range(n):
            nextInd = suffix[i][2] + k // 2
            suffix[i][1] = suffix[ind[nextInd]][0] if nextInd < n else -1
        
        suffix.sort()
        k *= 2
    
    return [v[2] for v in suffix]


# Complete the morganAndString function below.
def morganAndString(a, b):
    s = a + b
    suffix = suffixArray(s)
    rank = [0] * len(s)
    for i, v in enumerate(suffix):
        rank[v] = i
    ans = ''
    ia, ib = 0, 0
    na, nb = len(a), len(b)
    while ia < na and ib < nb:
        if rank[ia] < rank[na + ib]:
            ans += a[ia]
            ia += 1
        else:
            ans += b[ib]
            ib += 1
    
    if ia < na:
        ans += a[ia:]
    if ib < nb:
        ans += b[ib:]
    
    return ans


if __name__ == '__main__':
    print(morganAndString('JACK', 'DANIEL'))
