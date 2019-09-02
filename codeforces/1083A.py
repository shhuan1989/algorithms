# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/22 15:03

"""

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import networkx as nx
#
#
# def graph_visualize(g, arrows=False):
#     G = nx.DiGraph()
#
#     for u, vs in g.items():
#         for v in vs:
#             G.add_edge(u, v[0], weight=v[1])
#
#     # Need to create a layout when doing
#     # separate calls to draw nodes and edges
#     pos = nx.spring_layout(G)
#     nx.draw_networkx_nodes(G, pos)
#     nx.draw_networkx_labels(G, pos)
#     nx.draw_networkx_edges(G, pos, arrows=arrows)
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)]))
#     plt.show()

N = int(input())
W = [0] + [int(x) for x in input().split()]
G = collections.defaultdict(list)
C = {}
for i in range(N-1):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))
    C[(u, v)] = c
    C[(v, u)] = c


def gas(path):
    ans = 0

    i = 0
    n = len(path)
    u = path[0]
    g = W[u]
    while i + 1 < n:
        ans = max(ans, g)
        v = path[i+1]
        c = C[(u, v)]
        if g > c:
            g -= c
            g += W[v]
        else:
            g = W[v]
        u = v
        i += 1

    # print(path, ans)
    return max(ans, g)



def dfs(u, p, path):
    ans = 0
    for v, c in G[u]:
        if v != p:
            ans = max(ans, dfs(v, u, path+[v]))

    if ans == 0:
        # ans = max(gas(path), gas(list(reversed(path))))
        ans = gas(path)

    return ans

ans = max(W)
for i in range(1, N+1):
    ans = max(ans, dfs(i, -1, [i]))
print(ans)
