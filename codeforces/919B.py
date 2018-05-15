# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/2/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

K = int(input())


def construct(digits, numlen, rem):
  if len(digits) == numlen:
    return [int(''.join(map(str, digits)))]

  if len(digits) == numlen - 1:
    return [int(''.join(map(str, digits + [rem])))]

  ans = []
  start = 0 if digits else 1
  for i in range(start, min(rem+1, 10)):
    ans.extend(construct(digits+[i], numlen, rem - i))

  return ans

def find(numlen, kth):
  nums = construct([], numlen, 10)
  if len(nums) >= kth:
    return True, nums[kth-1]

  return False, len(nums)

def brutal_force(kth):
  val = 1
  k = 0
  while k < kth:
    val += 1
    if sum([int(x) for x in str(val)]) == 10:
      k += 1
      if k == kth:
        return val

def solve(kth):
  for numlen in range(2, 64):
    f, k = find(numlen, kth)
    if f:
      return k
    else:
      kth -= k

print(solve(K))
# print(construct([], 3, 10))

# for K in range(1, 10000):
#   v1 = brutal_force(K)
#   v2 = solve(K)
#   if v1 != v2:
#     print(v1, v2, K)
#     exit(0)
# for K in range(1, 100):
#
#   print(brutal_force(K))
#
#   for numlen in range(2, 64):
#     f, k = find(numlen, K)
#     if f:
#       print(k)
#       # exit(0)
#       break
#     else:
#       K -= k

