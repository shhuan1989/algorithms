# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/12

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    M = 1
    while 2 ** M <= N:
        M += 1
    
    pre = [[-1 for _ in range(M)] for _ in range(N)]
    preop = [[-1 for _ in range(M)] for _ in range(N)]
    num = [0 for _ in range(N)]
    A = []
    
    def find(index, k):
        # if k <= 0:
        #     return index+1
        # print(k)
        if k == 1:
            return pre[index][0]
        
        i = 0
        while 2 ** i <= k:
            i += 1
        i -= 1
        
        if 2 ** i == k:
            return pre[index][i]
        
        return find(pre[index][i]-1, k - 2**i)
    
    def findop(index, k):
        if k == 1:
            return preop[index][0]
        i = 0
        while 2 ** i <= k:
            i += 1
        i -= 2
        if 2 ** i == k:
            return preop[index][i]
        
        return findop(preop[index][i]-1, k - 2**i)
        

    i = -1
    for _ in range(N):
        o, v = input().strip().split()
        if o == 'T':
            A.append(v)
            i += 1
            num[i] = (num[i-1] if i-1 >= 0 else 0) + 1
            pre[i][0] = i
            for j in range(1, M):
                pi = pre[i][j-1] - 1
                if pi < 0:
                    break
                pre[i][j] = pre[pi][j-1]
                
            preop[i][0] = i
            for j in range(1, M):
                pi = preop[i][j-1] - 1
                if pi < 0:
                    break
                preop[i][j] = preop[pi][j-1]
                
        elif o == 'U':
            v = int(v)
            A.append('#')
            pi = findop(i, v) - 1
            i += 1
            num[i] = num[pi] if pi >= 0 else 0
            pre[i][0] = pre[pi][0] if pi >= 0 else -1
            for j in range(1, M):
                pi = pre[i][j-1] - 1
                if pi < 0:
                    break
                pre[i][j] = pre[pi][j-1]
            
            preop[i][0] = i
            for j in range(1, M):
                pi = preop[i][j-1] - 1
                if pi < 0:
                    break
                preop[i][j] = preop[pi][j-1]
            
        else:
            v = int(v)
            c = num[i]
            k = c - v + 1
            # print(A, v, c, k)
            if k <= 0:
                print(' ')
            else:
                print(A[find(i, k)])
            # print(A[v-1])
        