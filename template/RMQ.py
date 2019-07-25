# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-07-25

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math

class SegmentTree:
    """
    能更新和查询和、最大最小值
    """
    def __init__(self, size=1000):
        size = max(1000, size)
        size = min(1000000, size)
        self.sumTree = [0] * (4 * size)
        self.maxTree = [float('-inf')] * (4 * size)
    
    def build(self, A, index, l, r):
        """
        为数组A的闭区间[l, r]构建线段树
        :param A: 原始数组
        :param index: 当前节点在线段树数组中的位置下标
        :param l: 子区间的开始位置
        :param r: 子区间的结束位置
        :return:
        """
        if l == r:
            self.sumTree[index] = A[l]
            self.maxTree[index] = A[l]
        else:
            m = (l + r) // 2
            self.build(A, index * 2, l, m)
            self.build(A, index * 2 + 1, m + 1, r)
            self.sumTree[index] = self.sumTree[index * 2] + self.sumTree[index * 2 + 1]
            self.maxTree[index] = max(self.maxTree[index * 2], self.maxTree[index * 2 + 1])
    
    def sum(self, index, l, r, ql, qr):
        """
        在根节点是sumTree[index], 起始闭区间是[l, r]的线段树中查询闭区间[ql, qr]的和
        :param index: 当前线段树节点在数组中的位置下标
        :param l: 当前节点的区间开始位置
        :param r: 当前节点的区间结束位置
        :param ql: 查询区间的开始位置
        :param qr: 查询区间的结束位置
        :return:
        """
        if l > r or ql > qr:
            return 0
        
        if l == ql and r == qr:
            return self.sumTree[index]
        
        m = (l + r) // 2
        
        return self.sum(index * 2, l, m, ql, min(m, qr)) + self.sum(index * 2 + 1, m + 1, r, max(ql, m + 1), qr)
    
    def max(self, index, l, r, ql, qr):
        if l > r or ql > qr:
            return float('-inf')
        
        if l == ql and r == qr:
            return self.maxTree[index]
        
        m = (l + r) // 2
        return max(self.max(index * 2, l, m, ql, min(m, qr)), self.max(index * 2 + 1, m + 1, r, max(ql, m + 1), qr))
    
    def update(self, index, l, r, pos, val):
        """
        更新原始数组的值a[pos]=val，当前节点是区间[l, r]的和
        :param index: 当前节点在线段数组中的下标
        :param l: 区间开始位置
        :param r: 区间结束位置
        :param pos: 原始数组的下标
        :param val: 更新后的值
        :return:
        """
        if l == r:
            self.sumTree[index] = val
            self.maxTree[index] = val
        else:
            m = (l + r) // 2
            if pos <= m:
                self.update(index * 2, l, m, pos, val)
            else:
                self.update(index * 2 + 1, m + 1, r, pos, val)
            self.sumTree[index] = self.sumTree[index * 2] + self.sumTree[index * 2 + 1]
            self.maxTree[index] = max(self.maxTree[index * 2], self.maxTree[index * 2 + 1])

            
class FenwickTree:
    """
    能更新和查询和，不能处理区间最大最小值
    """
    def __init__(self):
        self.values = []
        self.bits = []
        self.size = 1000
        
    def build(self, A):
        self.size = max(len(A), self.size)
        self.bits = [0] * self.size
        self.values = [0] * self.size
        for i, v in enumerate(A):
            self.update(i, v)
            
    def sum(self, l, r):
        if l > r:
            return 0
        
        return self.sum_impl(r) - self.sum_impl(l-1)
    
    def update(self, pos, value):
        delta = value - self.values[pos]
        self.values[pos] = value
        self.add(pos, delta)
    
    def add(self, index, delta):
        while index < self.size:
            self.bits[index] += delta
            index |= index + 1

    def sum_impl(self, r):
        ans = 0
        while r >= 0:
            ans += self.bits[r]
            r = (r & (r + 1)) - 1
        
        return ans


class SparseTable:
    """
    能查询区间和、最大最小值，更新比较慢
    """
    
    def __init__(self):
        self.st = [[0]]
        self.mst = [[0]]
        self.k = 0
    
    def build(self, A):
        n = len(A)
        m = int(math.ceil(math.log(n, 2))) + 1
        self.k = m
        
        # st[i, j] will store the answer for the range [i,i+2^j−1] of length 2^j
        st = [[0 for _ in range(m)] for _ in range(n)]
        mst = [[float('-inf') for _ in range(m)] for _ in range(n)]
        for i, v in enumerate(A):
            st[i][0] = v
            mst[i][0] = v
        
        for j in range(1, m):
            for i in range(n - (1 << j) + 1):
                st[i][j] = st[i][j - 1] + st[i + (1 << (j - 1))][j - 1]
                mst[i][j] = max(mst[i][j - 1], mst[i + (1 << (j - 1))][j - 1])
        self.st = st
        self.mst = mst
    
    def sum(self, l, r):
        ans = 0
        for j in range(self.k, -1, -1):
            if r - l + 1 >= 1 << j:
                ans += self.st[l][j]
                l += 1 << j
        return ans
    
    def max(self, l, r):
        ans = float('-inf')
        for j in range(self.k, -1, -1):
            if r - l + 1 >= 1 << j:
                ans = max(ans, self.mst[l][j])
                l += 1 << j
        return ans
    
    def update(self, pos, value):
        pass
    

if __name__ == '__main__':
    s = SegmentTree()
    f = FenwickTree()
    st = SparseTable()
    A = [1, 3, -2, 8, -7]
    s.build(A, 1, 0, 4)
    f.build(A)
    st.build(A)
    for l in range(len(A)):
        for r in range((len(A))):
            print(l, r, s.sum(1, 0, 4, l, r), st.sum(l, r), s.sum(1, 0, 4, l, r) == st.sum(l, r))
    
    s.update(1, 0, 4, 2, 3)
    print('===========after=============')
    for l in range(len(A)):
        for r in range((len(A))):
            print(l, r, s.sum(1, 0, 4, l, r))