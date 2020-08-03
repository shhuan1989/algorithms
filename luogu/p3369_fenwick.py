# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/16

"""
import sys
import random
from memory_profiler import profile

INF = 10 ** 9 + 7
MAXN = 10**7+5


bits = [0 for _ in range(MAXN)]

def update(index, val):
    while index < MAXN:
        bits[index] += val
        index |= index + 1
    

def query(index):
    s = 0
    while index >= 0:
        s += bits[index]
        index = (index & (index + 1)) - 1
    
    return s


def searchk(k):
    lo, hi = 0, MAXN
    
    while lo <= hi:
        m = (lo + hi) // 2
        if query(m) >= k:
            hi = m - 1
        else:
            lo = m + 1
            
    return lo


def searchpre(x):
    k = query(x-1)
    return searchk(k)

def searchafter(x):
    k = query(x)
    return searchk(k+1)


@profile
def main():
    sys.stdin = open('p3369_3.in', 'r')
    N = int(input())
    ans = []
    id = 1
    root = 0
    for i in range(N):
        ops = [int(x) for x in input().strip().split()]
        op = ops[0]
        x = ops[1]
        if op == 1:
            update(x, 1)
            id += 1
        elif op == 2:
            update(x, - 1)
        elif op == 3:
            ans.append(query(x-1) + 1)
        elif op == 4:
            ans.append(searchk(x))
        elif op == 5:
            ans.append(searchpre(x))
        elif op == 6:
            ans.append(searchafter(x))
    print('\n'.join(map(str, ans)))
    

if __name__ == '__main__':
    main()