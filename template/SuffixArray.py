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


if __name__ == '__main__':
    print(suffixArray('banana'))