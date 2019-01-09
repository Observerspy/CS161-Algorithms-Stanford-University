import numpy as np
from collections import defaultdict
from heapq import heapify, heappop, heappush


def prim(nodes, edges):
    conn = defaultdict(list)
    for n1, n2, c in edges:
        conn[n1].append((c, n1, n2))
        conn[n2].append((c, n2, n1))

    mst = []
    used = set(nodes[0])
    usable_edges = conn[nodes[0]][:]
    heapify(usable_edges)

    while usable_edges:
        cost, n1, n2 = heappop(usable_edges)
        if n2 not in used:
            used.add(n2)
            mst.append((n1, n2, cost))

            for e in conn[n2]:
                if e[2] not in used:
                    heappush(usable_edges, e)
    return mst


if __name__ == '__main__':
    with open('prim.txt', 'r') as f:
        mylist = f.readlines()
    l = [np.array(i.split('\n')[0].split(' '), dtype=int) for i in mylist[1:]]
    E = []
    for a in l:
        E.append((str(a[0]), str(a[1]), int(a[2])))
    print('x')
    V = [str(i) for i in range(1,501)]
    # nodes = list("ABCDEFG")
    # edges = [("A", "B", 7), ("A", "D", 5),
    #          ("B", "C", 8), ("B", "D", 9),
    #          ("B", "E", 7), ("C", "E", 5),
    #          ("D", "E", 15), ("D", "F", 6),
    #          ("E", "F", 8), ("E", "G", 9),
    #          ("F", "G", 11)]

    mst = prim(V, E)
    print("cost", sum([m[2] for m in mst])) #-3612829