# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/22 15:33

"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx


def graph_visualize(g, arrows=False):
    G = nx.DiGraph()

    for u, vs in g.items():
        for v in vs:
            G.add_edge(u, v[0], weight=v[1])

    G.add_edges_from(
        [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
         ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=arrows)
    plt.show()
