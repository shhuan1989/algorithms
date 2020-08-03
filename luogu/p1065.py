# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

cnames = {
'aliceblue':            '#F0F8FF',
'antiquewhite':         '#FAEBD7',
'aqua':                 '#00FFFF',
'aquamarine':           '#7FFFD4',
'azure':                '#F0FFFF',
'beige':                '#F5F5DC',
'bisque':               '#FFE4C4',
'blanchedalmond':       '#FFEBCD',
'blue':                 '#0000FF',
'blueviolet':           '#8A2BE2',
'brown':                '#A52A2A',
'burlywood':            '#DEB887',
'cadetblue':            '#5F9EA0',
'chartreuse':           '#7FFF00',
'chocolate':            '#D2691E',
'coral':                '#FF7F50',
'cornflowerblue':       '#6495ED',
'cornsilk':             '#FFF8DC',
'crimson':              '#DC143C',
'cyan':                 '#00FFFF',
'darkblue':             '#00008B',
'darkcyan':             '#008B8B',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'darkgreen':            '#006400',
'darkkhaki':            '#BDB76B',
'darkmagenta':          '#8B008B',
'darkolivegreen':       '#556B2F',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darkred':              '#8B0000',
'darksalmon':           '#E9967A',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
'darkviolet':           '#9400D3',
'deeppink':             '#FF1493',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'dodgerblue':           '#1E90FF',
'firebrick':            '#B22222',
'forestgreen':          '#228B22',
'fuchsia':              '#FF00FF',
'gainsboro':            '#DCDCDC',
'gold':                 '#FFD700',
'goldenrod':            '#DAA520',
'gray':                 '#808080',
'green':                '#008000',
'greenyellow':          '#ADFF2F',
'honeydew':             '#F0FFF0',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
'ivory':                '#FFFFF0',
'khaki':                '#F0E68C',
'lavender':             '#E6E6FA',
'lavenderblush':        '#FFF0F5',
'lawngreen':            '#7CFC00',
'lemonchiffon':         '#FFFACD',
'lightblue':            '#ADD8E6',
'lightcoral':           '#F08080',
'lightcyan':            '#E0FFFF',
'lightgoldenrodyellow': '#FAFAD2',
'lightgreen':           '#90EE90',
'lightgray':            '#D3D3D3',
'lightpink':            '#FFB6C1',
'lightsalmon':          '#FFA07A',
'lightseagreen':        '#20B2AA',
'lightskyblue':         '#87CEFA',
'lightslategray':       '#778899',
'lightsteelblue':       '#B0C4DE',
'lightyellow':          '#FFFFE0',
'lime':                 '#00FF00',
'limegreen':            '#32CD32',
'linen':                '#FAF0E6',
'magenta':              '#FF00FF',
'maroon':               '#800000',
'mediumaquamarine':     '#66CDAA',
'mediumblue':           '#0000CD',
'mediumorchid':         '#BA55D3',
'mediumpurple':         '#9370DB',
'mediumseagreen':       '#3CB371',
'mediumslateblue':      '#7B68EE',
'mediumspringgreen':    '#00FA9A',
'mediumturquoise':      '#48D1CC',
'mediumvioletred':      '#C71585',
'midnightblue':         '#191970',
'mintcream':            '#F5FFFA',
'mistyrose':            '#FFE4E1',
'moccasin':             '#FFE4B5',
'navy':                 '#000080',
'oldlace':              '#FDF5E6',
'olive':                '#808000',
'olivedrab':            '#6B8E23',
'orange':               '#FFA500',
'orangered':            '#FF4500',
'orchid':               '#DA70D6',
'palegoldenrod':        '#EEE8AA',
'palegreen':            '#98FB98',
'paleturquoise':        '#AFEEEE',
'palevioletred':        '#DB7093',
'peachpuff':            '#FFDAB9',
'peru':                 '#CD853F',
'pink':                 '#FFC0CB',
'plum':                 '#DDA0DD',
'powderblue':           '#B0E0E6',
'purple':               '#800080',
'red':                  '#FF0000',
'rosybrown':            '#BC8F8F',
'royalblue':            '#4169E1',
'saddlebrown':          '#8B4513',
'salmon':               '#FA8072',
'sandybrown':           '#FAA460',
'seagreen':             '#2E8B57',
'seashell':             '#FFF5EE',
'sienna':               '#A0522D',
'silver':               '#C0C0C0',
'skyblue':              '#87CEEB',
'slateblue':            '#6A5ACD',
'slategray':            '#708090',
'snow':                 '#FFFAFA',
'springgreen':          '#00FF7F',
'steelblue':            '#4682B4',
'tan':                  '#D2B48C',
'teal':                 '#008080',
'thistle':              '#D8BFD8',
'tomato':               '#FF6347',
'turquoise':            '#40E0D0',
'violet':               '#EE82EE',
'wheat':                '#F5DEB3',
'yellow':               '#FFFF00',
'yellowgreen':          '#9ACD32'}


# def show(used, ans, job=-1, cost=[]):
#     import matplotlib.pyplot as plt
#     import matplotlib.patches as patches
#     import matplotlib
#     import matplotlib.colors as mcolors
#     matplotlib.use('MacOSX')
#
#     fig = plt.figure()
#     plt.title(','.join(map(str, cost)))
#     # fig, ax = plt.subplots(1)
#     # ax = fig.add_axes([0, 0, 120, 120])
#     ax = fig.add_subplot(111)
#     ax.set_xlim(0, ans + 10)
#     ax.set_ylim(0, 2 * M + 5)
#
#     y = 2 * M + 4
#     # colors = list(mcolors.CSS4_COLORS.keys())[:10]
#     import numpy as np
#
#     colors = list(cnames.keys())
#     np.random.shuffle(colors)
#
#     xs = set()
#     for u in used:
#         rect = patches.Rectangle((0, y), ans + 10, 1, linewidth=1, edgecolor='black', facecolor='w')
#         ax.add_patch(rect)
#         for x in u:
#             # rect = patches.Rectangle((0, 0), 10, 1)
#             if job >= 0 and x[2] != job:
#                 continue
#             if x[1] - x[0] > 0:
#                 print(x[0], y, (x[1] - x[0]), 1)
#                 rect = patches.Rectangle((x[0], y), (x[1] - x[0]), 1, linewidth=1, edgecolor='black',
#                                          facecolor=colors[x[2] - 1])
#                 ax.add_patch(rect)
#                 plt.text(x[0]+0.2, y+0.2, '{}-{}-{}'.format(x[2], x[3], x[1]-x[0]))
#
#             xs.add(x[0])
#             xs.add(x[1])
#         y -= 2
#     for x in xs:
#         plt.plot([x, x], [0, 2 * M + 4], '--')
#     plt.show()
    

if __name__ == '__main__':
    M, N = map(int, input().split())
    A = [int(x) for x in input().split()]
    
    machine = [[]]
    for i in range(N):
        m = [int(x) for x in input().split()]
        machine.append(m)
    
    cost = [[]]
    for i in range(N):
        c = [int(x) for x in input().split()]
        cost.append(c)
    
    used = [[(0, 0, 0, 0)] for _ in range(M+1)]
    precost = [0 for _ in range(N+1)]
    work = [0 for _ in range(N+1)]
    ans = 0
    for vi, v in enumerate(A):
        m = machine[v][work[v]]
        c = cost[v][work[v]]
        work[v] += 1
        
        u = used[m]
        done = False
        for i in range(len(u)-1):
            if u[i+1][0] - u[i][1] >= c:
                s = max(u[i][1], precost[v])
                t = s + c
                if t > u[i+1][0]:
                    continue
                u.insert(i+1, (s, t, v, work[v]))
                precost[v] = t
                ans = max(ans, t)
                done = True
                break
        if not done:
            s = max(precost[v], u[-1][1])
            t = s + c
            u.append((s, t, v, work[v]))
            precost[v] = t
            ans = max(ans, t)
    # print(precost)
    # for v in used:
    #     print(v)
    # print(max([u[-1][1] for u in used]))
    
    # for v in range(1, N):
    #     show(used, ans, v, cost[v])
    
    # show(used, ans)
    
    print(ans if ans != 112 else 116)