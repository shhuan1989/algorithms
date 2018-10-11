# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/28/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N = int(input())

A = [int(x) for x in input()]

res = False
for target in range(1000):
    
    left = 0
    currentSum = 0
    valid = True
    count = 0
    
    while left < len(A):
        currentSum += A[left]
        if currentSum > target:
            valid = False
            break
        if left == len(A) - 1:
            if currentSum == target:
                count += 1
            elif currentSum != 0:
                valid = False
                
            break
            
        if currentSum == target:
            count += 1
            currentSum = 0
        left += 1
    
    if count < 2:
        valid = False
    
    if valid:
        res = True
        break
        
if res:
    print('YES')
else:
    print('NO')
    
    

