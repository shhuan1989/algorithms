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
created by shhuan at 2017/11/19 21:52




如果K==-1且N，M的奇偶性不同，没有满足条件的矩阵，输出0。
假设N是偶数，M是奇数。
N行，每一行都有奇数个-1，-1的总数量是偶数，因为偶数个奇数相加是偶数。
偶数个-1分布到奇数（M）个列，不可能每一列都是奇数，矛盾。


设A是整个矩阵，B是前N-1行，M-1列
对于其他情况，B可以任意填，总共2^((M-1)*(N-1)种可能。

对于任意一种情况，每一行和每一列的最后一个数字都能唯一确定。

需要证明最右下角的数字也是确定的，而不会矛盾。

假设K==1，对于前N-1行，前M-1列：
1. B有奇数个-1， 那A最后一列除了右下角的部分，有奇数个-1，A最后一行前M-1个也是奇数个-1。
    A最右下角应该是-1。
2. B有偶数个-1，右边，下边也该是偶数个-1，最后一个数字应更是1。



"""

MOD = 1000000007

N, M, K = map(int, input().split())


def my_pow_2(x):
    if x == 0:
        return 1

    h = my_pow_2(x//2)
    if x & 1:
        return (h*h*2) % MOD
    else:
        return (h*h) % MOD

if K == -1 and N%2 != M%2:
    print(0)
else:
    print(my_pow_2((N-1)*(M-1)))