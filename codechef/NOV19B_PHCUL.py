# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math


class KdTreeNode:
    def __init__(self, x, parent=None, split_by=None, split_feature_val_range=None, feature_max=None,
                 feature_min=None, left=None, right=None):
        self.X = x
        self.parent = parent
        self.left = left
        self.right = right
        self.split_by = split_by
        self.split_feature_val_range = split_feature_val_range
        self.feature_max = feature_max
        self.feature_min = feature_min
        self.level = -1
        self.id = -1


def build_kd_tree(X, feature_index):
    if not X:
        return None
    
    split_by = feature_index % 2
    split_val = [v[split_by] for v in X]
    
    feature_max = max(split_val)
    feature_min = min(split_val)
    split_feature_val_range = '({:.2f},{:.2f})'.format(feature_min, feature_max)
    
    val_index = [(v, i) for i, v in enumerate(split_val)]
    val_index.sort()
    
    sorted_index = [i for v, i in val_index]
    median_index = len(sorted_index) // 2
    
    node = KdTreeNode(X[sorted_index[median_index]], split_by=feature_index % 2,
                      split_feature_val_range=split_feature_val_range,
                      feature_max=feature_max, feature_min=feature_min)
    
    leftX, rightX = [X[i] for i in sorted_index[:median_index]], [X[i] for i in sorted_index[median_index+1:]]
    
    # 分别为小于和大于中位数的样本构建为左右子树
    node.left = build_kd_tree(leftX, feature_index + 1)
    node.right = build_kd_tree(rightX, feature_index + 1)
    if node.left:
        node.left.parent = node
    if node.right:
        node.right.parent = node
    
    return node


def set_node_id(treeNode, start):
    q = [(treeNode, 1)]
    while q:
        node, level = q[0]
        while q and q[0][1] == level:
            node, _ = q.pop(0)
            node.id = start
            node.level = level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
            start += 1

    return start

def search_leaf(root: KdTreeNode, target):
    node = root
    while True:
        if not node.left and not node.right:
            break

        fi = node.split_by
        if target[fi] <= node.X[fi]:
            if node.left:
                node = node.left
            else:
                node = node.right
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
                
    return node


def dist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def search(node, target):
    # 找到叶子结点,作为当前最近的点
    leaf = search_leaf(node, target)
    ans = leaf
    mindist = dist(leaf.X, target)

    q = [leaf]
    # vis用于确保每个结点只入队列一次
    vis = {leaf.id}
    while q:
        node = q.pop()
        d = dist(node.X, target)
        if d < mindist:
            mindist = d
            ans = node

        parent = node.parent
        if not parent:
            continue

        # 回退到父结点
        if parent.id not in vis:
            vis.add(parent.id)
            q.append(parent)

        # 检查兄弟结点
        sib = parent.left if node != parent.left else parent.right
        if not sib or sib.id in vis:
            continue

        hyperplate = parent.split_by
        # 到超平面的距离, 因为分割平面只分割了某一个维度,所以距离是那个维度的坐标直接相减
        hyperdist = abs(parent.X[hyperplate] - target[hyperplate])
        # 到超平面的距离小于当前最小距离,那个兄弟结点所在的空间中可能存在更近的点,使兄弟结点入队列
        if hyperdist < mindist:
            sibleaf = search_leaf(sib, target)
            if sibleaf.id not in vis:
                vis.add(sibleaf.id)
                q.append(sibleaf)

    return ans, mindist


def search_k(node, target, k):
    # 找到叶子结点,作为当前最近的点
    leaf = search_leaf(node, target)
    q = [leaf]
    kmin = []
    heapq.heapify(kmin)
    # vis用于确保每个结点只入队列一次
    vis = {leaf.id}
    
    while q:
        node = q.pop()
        d = dist(node.X, target)
        if len(kmin) < k:
            heapq.heappush(kmin, (-d, node))
        elif d < abs(kmin[0][0]):
            heapq.heappop(kmin)
            heapq.heappush(kmin, (-d, node))
        
        parent = node.parent
        if not parent:
            continue
        
        # 回退到父结点
        if parent.id not in vis:
            vis.add(parent.id)
            q.append(parent)
        
        # 检查兄弟结点
        sib = parent.left if node != parent.left else parent.right
        if not sib or sib.id in vis:
            continue
        
        hyperplate = parent.split_by
        # 到超平面的距离, 因为分割平面只分割了某一个维度,所以距离是那个维度的坐标直接相减
        hyperdist = abs(parent.X[hyperplate] - target[hyperplate])
        # 到超平面的距离小于当前最小距离,那个兄弟结点所在的空间中可能存在更近的点,使兄弟结点入队列
        if hyperdist < abs(kmin[0][0]):
            sibleaf = search_leaf(sib, target)
            if sibleaf.id not in vis:
                vis.add(sibleaf.id)
                q.append(sibleaf)
    
    ans = []
    while kmin:
        d, node = heapq.heappop(kmin)
        ans.append((abs(d), node))
    return list(reversed(ans))

def solve(start, kdab, kdef, cd):
    ans = float('inf')
    for x, y in cd:
        d3 = search(kdef, (x, y))
        
        mid = ((start[0]+x)/2, (start[1]+y)/2)
        
        node, d2 = search(kdab, mid)
        d1 = dist(start, node.X)
        
        d = d1 + d2 + d3
        ans = min(ans, d)
    
    return ans
    


T = int(input())
ans = []
for ti in range(T):
    x, y = map(int, input().split())
    N, M, K = map(int, input().split())
    ab = [int(x) for x in input().split()]
    cd = [int(x) for x in input().split()]
    ef = [int(x) for x in input().split()]
    
    ab = [(ab[2*i], ab[2*i+1]) for i in range(len(ab)//2)]
    cd = [(cd[2 * i], cd[2 * i + 1]) for i in range(len(cd) // 2)]
    ef = [(ef[2 * i], ef[2 * i + 1]) for i in range(len(ef) // 2)]
    
    kdab = build_kd_tree(ab, 0)
    kdcd = build_kd_tree(cd, 0)
    kdef = build_kd_tree(ef, 0)
    
    ans.append(min(solve((x, y), kdab, kdef, cd), solve((x, y), kdcd, kdef, ab)))

print('\n'.join(map(str, ans)))




# import random
#
# X = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(50)]
# kdTree = build_kd_tree(X, 0)
# set_node_id(kdTree, 1)
# print(X)
# target = (random.randint(0, 10), random.randint(0, 10))
# k = search_leaf(kdTree, target)
# print(k)
#
# t, d = search(kdTree, target)
#
#
#
# import matplotlib.pyplot as plt
#
# plt.figure()
# plt.title('{:.2f}'.format(d))
# plt.scatter([v[0] for v in X], [v[1] for v in X], c='blue')
# plt.scatter([target[0]], [target[1]], c='r')
#
# plt.scatter([k.X[0]], [k.X[1]], c='g')
# plt.scatter([t.X[0]], [t.X[1]], c='y')
#
# plt.show()