# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-05-15

"""

import collections
import time
import os
import sys
import bisect
import heapq
import matplotlib.pyplot as plt
import networkx as nx



if __name__ == '__main__':
    
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    edgs = []
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        edgs.append((u, v))

    graph = nx.DiGraph(directed=True)
    graph.add_edges_from(edgs)
    nx.draw(graph, with_labels=True)
    plt.draw()
    plt.show()
    
    