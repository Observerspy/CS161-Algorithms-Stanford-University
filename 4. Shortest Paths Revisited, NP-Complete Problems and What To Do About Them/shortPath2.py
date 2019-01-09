import sys
INF = 999999
import copy
from collections import defaultdict
from heapq import *
import numpy as np
from tqdm import trange
def dijkstra(edges, from_node):
    d = {}
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            d[v1] = cost
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return d


def bellman_ford(E, source, vnum):
    dist = {}
    p = {}
    for v in range(vnum):
        dist[v] = INF  # 赋值为负无穷完成初始化
        p[v] = None
    dist[source] = 0

    for i in range(vnum - 1):
        for e in E:
            if dist[e[2]] > e[0] + dist[e[1]]:
                dist[e[2]] = e[0] + dist[e[1]]
                p[e[2]] = e[1]  # 完成松弛操作，p为前驱节点

    for e in E:
        if dist[e[2]] > dist[e[1]] + e[0]:
            return None, None  # 判断是否存在环路

    return dist, p


if __name__ == '__main__':
    with open('large.txt', 'r') as f:
        mylist = f.readlines()
    a = [np.array(str.split('\n')[0].split(' '), dtype=int) for str in mylist[1:]]
    E = []
    for l in a:
        E.append((l[2], l[0], l[1]))
    E_old = copy.deepcopy(E)
    vnum = 20000
    for i in range(vnum):
        E.append((0, 0, i+1))
    dist, p = bellman_ford(E, 0, vnum+1)
    print(dist)
    E_reweight = []
    for e in E_old:
        E_reweight.append((e[1], e[2], e[0] + dist[e[1]] - dist[e[2]]))
    # print(E_reweight)
    d = np.zeros((vnum, vnum))
    for i in trange(vnum):
        cost = dijkstra(E_reweight, i+1)
        for key,val in cost.items():
            d[i][key-1] = val + dist[key] - dist[i+1]
    print(np.min(d))