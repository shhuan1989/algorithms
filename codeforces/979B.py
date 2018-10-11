# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 5/15/18

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
a = input()
b = input()
c = input()

# N = random.randint(10**4, 10**5)
# a = "".join([chr(ord('a')+random.randint(0, 52)) for _ in range(10**5)])
# b = "".join([chr(ord('a')+random.randint(0, 52)) for _ in range(10**5)])
# c = "".join([chr(ord('a')+random.randint(0, 52)) for _ in range(10**5)])

t0 = time.time()

def change(colors, steps):
  cc = set(colors)
  wc = collections.Counter(colors)

  res = 0
  for c in cc:
    left = len(colors) - wc[c]
    if steps <= left:
      res = max(res, wc[c] + steps)
    else:
      if (steps-left) % 2 == 0:
        return len(colors)
      else:
        res = max(res, len(colors)-1)
  return res



bs = [change(x, N) for x in [a, b, c]]

mx = max(bs)
if len([x for x in bs if x == mx]) >= 2:
  print("Draw")
elif mx == bs[0]:
  print("Kuro")
elif mx == bs[1]:
  print("Shiro")
else:
  print("Katie")



# print(time.time() - t0)



