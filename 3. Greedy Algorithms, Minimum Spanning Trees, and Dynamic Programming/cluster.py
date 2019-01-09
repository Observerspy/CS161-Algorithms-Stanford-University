import numpy as np
from collections import defaultdict
from heapq import heapify, heappop, heappush
class MySet():
    def __init__(self, par, rank):
        self.parent = par
        self.rank = rank


def find(a, i):
    if a[i].parent != i:
        a[i].parent = find(a, a[i].parent)
    return a[i].parent


def union(a, x, y):
    xroot = find(a, x)
    yroot = find(a, y)
    if a[xroot].rank < a[yroot].rank :
        a[xroot].parent = yroot
    elif a[xroot].rank > a[yroot].rank :
        a[yroot].parent = xroot
    else:
        a[yroot].parent = xroot
        a[xroot].rank += 1


if __name__ == '__main__':
    with open('cluster.txt', 'r') as f:
        mylist = f.readlines()
    a = [np.array(str.split('\n')[0].split(' '), dtype=int) for str in mylist[1:]]
    E = []
    for l in a:
        E.append((l[2], l[0], l[1]))
    heapify(E)
    v_num = 500
    k = 4
    s = []
    for i in range(v_num):
        o = MySet(i, 0)
        s.append(o)

    while v_num > k:
        cost, n1, n2 = heappop(E)
        set1 = find(s, n1-1)
        set2 = find(s, n2-1)

        if set1 == set2:
            continue
        else:
            v_num -= 1
            union(s, set1, set2)

    count = 0
    d = {}
    for i in range(len(E)):
        set1 = find(s, E[i][1]-1)
        set2 = find(s, E[i][2]-1)
        if set1 != set2:
            val = d.setdefault(str(set1) + '-' + str(set2), 99999)
            if val >= E[i][0]:
               d[str(set1)+'-'+str(set2)] = E[i][0]
    # print(set([find(s, i) for i in range(500)]))
    print([v for v in sorted(d.values())][0]) #106

