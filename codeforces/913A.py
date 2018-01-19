# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/11/18

"""

import math

N = int(input())
M = int(input())

if N > int(math.log2(10**8)):
  print(M)
else:
  print(M % (2**N))
